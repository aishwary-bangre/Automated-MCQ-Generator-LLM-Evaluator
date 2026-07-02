import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def evaluate_mcq(context: str, mcq_json: str) -> dict:
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
        timeout=30.0
    )
    system_prompt = """You are an expert educational evaluator. 
Your job is to evaluate a generated Multiple Choice Question based on the provided context.
You must output ONLY valid JSON containing your evaluation scores and feedback.

Rate the MCQ on three criteria (1-10 scale):
1. hallucination_score: 10 means NO hallucinations. Note: Introducing generic variables (like points P and Q, or names) and new numbers to create a valid math problem is normal and is NOT a hallucination. Only penalize if the question contradicts the provided context's core concepts.
2. logic_score: 10 means the math and logic are perfectly sound.
3. plausibility_score: 10 means the distractors (wrong answers) are highly plausible student mistakes.

Return EXACTLY this JSON format:
{
  "hallucination_score": 10,
  "logic_score": 10,
  "plausibility_score": 10,
  "overall_score": 10,
  "feedback": "Your concise explanation here."
}"""

    user_prompt = f"CONTEXT:\n{context}\n\nGENERATED MCQ JSON:\n{mcq_json}\n\nEvaluate the MCQ against the context and provide the JSON output."

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

