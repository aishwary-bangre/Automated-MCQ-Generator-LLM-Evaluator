import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def evaluate_mcq(topic: str, context: str, mcq_json: str) -> dict:
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
        timeout=30.0
    )
    system_prompt = """You are a Senior Educational Assessor and LLM Evaluation Expert.
Your objective is to rigorously grade an AI-generated Multiple Choice Question (MCQ) against the provided source CONTEXT and target TOPIC.
You must act as a deterministic scoring engine. Output ONLY valid JSON, with no conversational text.

Grading Rubric (1-10 scale):
1. hallucination_score (10 = Perfect, 0 = Complete Hallucination): 
   - Score 10 if every mathematical fact and premise in the question is supported by the CONTEXT or TOPIC.
   - Score 5 if it introduces external formulas not present in the CONTEXT.
   - Score 0 if the question contradicts the CONTEXT entirely.
   
2. logic_score (10 = Perfect, 0 = Illogical): 
   - Score 10 if the 'correct answer' is mathematically flawless and the explanation logically derives it.
   - Score 0 if the math is wrong, or if multiple options could be considered correct.
   
3. plausibility_score (10 = Perfect, 0 = Trivial): 
   - Score 10 if all 3 distractors target distinct, common mathematical errors (e.g., sign drops, conceptual failures).
   - Score 0 if distractors are obvious joke answers or trivial random numbers.

Calculate an 'overall_score' as the exact average of the three.

Return EXACTLY this JSON format:
{
  "hallucination_score": 10,
  "logic_score": 10,
  "plausibility_score": 10,
  "overall_score": 10.0,
  "feedback": "Detailed justification citing specific elements of the context or distractors to explain your scores."
}"""

    user_prompt = f"TOPIC: {topic}\n\nCONTEXT:\n{context}\n\nGENERATED MCQ JSON:\n{mcq_json}\n\nEvaluate the MCQ against the topic and context and provide the JSON output."

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.0,
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"Error parsing Judge output: {e}")
        return {
            "hallucination_score": 0, "logic_score": 0, "plausibility_score": 0, "overall_score": 0,
            "feedback": f"Failed to parse JSON: {str(e)}"
        }

