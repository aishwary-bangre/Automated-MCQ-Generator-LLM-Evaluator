import os
import json
import random
from google import genai
from google.genai import types
from dotenv import load_dotenv
from src.rag.retrieval import retrieve_context
from src.agents.schemas import EducatorOutput, SpecialistOutput, FinalMCQ

load_dotenv()

def run_agent_1(topic: str, context: str, client: genai.Client):
    system_instruction = "You are an expert Math Educator. You must output ONLY valid JSON."
    prompt = f'Using the provided textbook context, you MUST generate a math question specifically focused on the sub-topic: "{topic}".\nDo NOT generate a generic question. The question must test the student\'s knowledge of "{topic}".\n\nContext:\n{context}\n\nOutput JSON format:\n{{\n  "question": "your math question here",\n  "correct_answer_text": "the correct answer here",\n  "explanation": "step-by-step solution here"\n}}'

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.3,
            response_mime_type="application/json",
        ),
    )
    data = json.loads(response.text)
    return EducatorOutput(**data), response.usage_metadata.prompt_token_count, response.usage_metadata.candidates_token_count

def run_agent_2(educator_output: EducatorOutput, client: genai.Client):
    system_instruction = "You are an expert in student misconceptions. You must output ONLY valid JSON."
    prompt = f'Generate 3 plausible wrong answers for this math question based on common mistakes.\n\nQuestion: {educator_output.question}\nCorrect Answer: {educator_output.correct_answer_text}\n\nOutput JSON format:\n{{\n  "distractors": [\n    {{"distractor_text": "wrong 1", "misconception": "reason 1"}},\n    {{"distractor_text": "wrong 2", "misconception": "reason 2"}},\n    {{"distractor_text": "wrong 3", "misconception": "reason 3"}}\n  ]\n}}'

    response = client.models.generate_content(
        model='gemini-3.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.5,
            response_mime_type="application/json",
        ),
    )
    data = json.loads(response.text)
    return SpecialistOutput(**data), response.usage_metadata.prompt_token_count, response.usage_metadata.candidates_token_count

def generate_mcq_pipeline(topic: str):
    print(f"Retrieving context for: {topic}")
    context = retrieve_context(topic, n_results=2)
    client = genai.Client(http_options={'timeout': 60.0})
    print("Agent 1 (Educator) generating question...")
    educator_out, e_in, e_out = run_agent_1(topic, context, client)
    print("Agent 2 (Specialist) generating distractors...")
    specialist_out, s_in, s_out = run_agent_2(educator_out, client)
    total_in = e_in + s_in
    total_out = e_out + s_out
    
    all_options = [educator_out.correct_answer_text] + [d.distractor_text for d in specialist_out.distractors]
    random.shuffle(all_options)
    
    correct_letter = ""
    options_map = {}
    for i, opt in enumerate(all_options):
        letter = chr(65 + i)
        options_map[letter] = opt
        if opt == educator_out.correct_answer_text: correct_letter = letter
            
    rich_explanation = f"{educator_out.explanation}\n\n**Mistakes:**\n"
    for d in specialist_out.distractors:
        rich_explanation += f"- {d.distractor_text}: {d.misconception}\n"
            
    mcq = FinalMCQ(
        question=educator_out.question,
        option_a=options_map["A"], option_b=options_map["B"], option_c=options_map["C"], option_d=options_map["D"],
        correct_answer=correct_letter, explanation=rich_explanation
    )
    return mcq, total_in, total_out
