import json
import re
import random
import os

# Force HuggingFace to use the D drive for all model downloads!
os.environ["HF_HOME"] = r"D:\huggingface_cache"
# Bypass CVE-2025-32434 block on PyTorch 2.5 — safe for trusted HuggingFace models
os.environ["TORCH_FORCE_WEIGHTS_ONLY_WARN_ONLY"] = "1"

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from .schemas import EducatorOutput, SpecialistOutput, FinalMCQ
from src.rag.retrieval import retrieve_context

# Qwen2.5-0.5B-Instruct: instruction-tuned model that actually follows prompts
MODEL_NAME = r"D:\huggingface_cache\Qwen2.5-0.5B-Instruct"
tokenizer = None
model = None

def load_model():
    global tokenizer, model
    if model is None:
        print(f"Loading {MODEL_NAME} into GPU VRAM...")
        
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        
        # 1.5B params in float16 = ~1GB. We FORCE it to 'cuda' to stop 'auto' from offloading to slow RAM.
        # We also enable 'sdpa' (Scaled Dot Product Attention) to drastically speed up generation.
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME, 
            torch_dtype=torch.float16,
            device_map="cuda", 
            attn_implementation="sdpa",
            low_cpu_mem_usage=True
        )
        print("Model loaded successfully on GPU!")

def generate_chat(system_prompt: str, user_prompt: str, max_tokens: int = 500):
    """Generate a response using Qwen's chat template and return (text, input_tokens, output_tokens)."""
    load_model()
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(text, return_tensors="pt").to("cuda")
    
    input_tokens = inputs["input_ids"].shape[1]
    
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_tokens,
        do_sample=False
    )
    
    # Only decode the NEW tokens (skip the prompt)
    new_tokens = outputs[0][input_tokens:]
    output_tokens = len(new_tokens)
    return tokenizer.decode(new_tokens, skip_special_tokens=True), input_tokens, output_tokens

def extract_json_from_text(text: str) -> dict:
    import re
    import json
    
    # 1. Clean common LaTeX block issues
    text = text.replace(r'\(', '(').replace(r'\)', ')')
    text = text.replace(r'\[', '[').replace(r'\]', ']')
    
    # 2. Find anything that looks like { ... }
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if not match:
        raise ValueError(f"No JSON found in output: {text[:200]}")
        
    fragment = match.group(0)
    
    # 3. Aggressively sanitize the fragment to force it into valid JSON
    # Replace all backslashes with double backslashes for valid escaping
    clean = fragment.replace('\\', '\\\\')
    # Re-fix valid escapes that got double-escaped
    clean = clean.replace('\\\\"', '\\"')
    clean = clean.replace('\\\\n', '\\n')
    # Remove literal newlines which crash JSON strings
    clean = clean.replace('\n', ' ')
    
    try:
        return json.loads(clean)
    except Exception as e:
        # Fallback: AST literal eval (handles Python-like dicts)
        import ast
        try:
            return ast.literal_eval(fragment)
        except:
            raise ValueError(f"Failed to parse JSON from output: {fragment}")

def run_local_agent_1(topic: str, context: str):
    """Agent 1: Educator Pipeline on local GPU model"""
    system = "You are an expert Math Educator. You output ONLY valid JSON, no markdown, no other text. IMPORTANT: Wrap ALL mathematical expressions and variables in single dollar signs (e.g., $x = 5$ or $\\frac{1}{2}$)."
    
    user = f"""Using the provided textbook context, you MUST generate a math question specifically focused on the sub-topic: "{topic}".
Do NOT generate a generic question. The question must test the student's knowledge of "{topic}".

Context:
{context}

You must output a single JSON object. Here is an EXAMPLE of the format you must use (do NOT copy this content, only the format):
{{
  "question": "your math question here",
  "correct_answer_text": "the correct answer here",
  "explanation": "step-by-step solution here"
}}

Generate the JSON object for "{topic}" now:"""
    
    response, in_t, out_t = generate_chat(system, user, max_tokens=1000)
    try:
        data = extract_json_from_text(response)
    except Exception as e:
        print(f"\n--- RAW QWEN AGENT 1 OUTPUT ---\n{response}\n------------------------------\n")
        raise e
    return EducatorOutput(**data), in_t, out_t

def run_local_agent_2(educator_output: EducatorOutput):
    """Agent 2: Specialist Pipeline on local GPU model"""
    system = "You are an expert in student misconceptions. You output ONLY valid JSON, no markdown, no other text. IMPORTANT: Wrap ALL mathematical expressions and variables in single dollar signs (e.g., $x = 5$ or $\\frac{1}{2}$)."
    
    user = f"""Generate 3 plausible wrong answers for this math question. Each wrong answer should reflect a common student mistake.

Question: {educator_output.question}
Correct Answer: {educator_output.correct_answer_text}

You must output a single JSON object. Here is an EXAMPLE of the format you must use (do NOT copy this content, only the format):
{{
  "distractors": [
    {{"distractor_text": "wrong 1", "misconception": "reason 1"}},
    {{"distractor_text": "wrong 2", "misconception": "reason 2"}},
    {{"distractor_text": "wrong 3", "misconception": "reason 3"}}
  ]
}}

Generate the JSON object for the distractors now:"""

    response, in_t, out_t = generate_chat(system, user, max_tokens=1000)
    try:
        data = extract_json_from_text(response)
        if "distractors" in data and isinstance(data["distractors"], list):
            while len(data["distractors"]) < 3:
                data["distractors"].append({
                    "distractor_text": "None of the above",
                    "misconception": "Generic incorrect option due to generation failure."
                })
    except Exception as e:
        print(f"\n--- RAW QWEN AGENT 2 OUTPUT ---\n{response}\n------------------------------\n")
        raise e
    return SpecialistOutput(**data), in_t, out_t

def generate_qwen_mcq(topic: str):
    """Retrieves context and runs the dual-agent pipeline to return a perfectly formatted MCQ."""
    print(f"Retrieving context for: {topic}")
    context = retrieve_context(topic, n_results=2)
    
    print("Local Agent 1 generating question...")
    educator_out, e_in, e_out = run_local_agent_1(topic, context)
    
    print("Local Agent 2 generating distractors...")
    specialist_out, s_in, s_out = run_local_agent_2(educator_out)
    
    total_in = e_in + s_in
    total_out = e_out + s_out
    
    # Combine and shuffle options
    all_options = [educator_out.correct_answer_text] + [d.distractor_text for d in specialist_out.distractors]
    random.shuffle(all_options)
    
    correct_letter = ""
    options_map = {}
    for i, opt in enumerate(all_options):
        letter = chr(65 + i) # A, B, C, D
        options_map[letter] = opt
        if opt == educator_out.correct_answer_text:
            correct_letter = letter
            
    # Add misconception data into the explanation
    rich_explanation = f"{educator_out.explanation}\n\n**Mistakes:**\n"
    for d in specialist_out.distractors:
        rich_explanation += f"- {d.distractor_text}: {d.misconception}\n"
            
    mcq = FinalMCQ(
        question=educator_out.question,
        option_a=options_map["A"],
        option_b=options_map["B"],
        option_c=options_map["C"],
        option_d=options_map["D"],
        correct_answer=correct_letter,
        explanation=rich_explanation
    )
    return mcq, total_in, total_out
