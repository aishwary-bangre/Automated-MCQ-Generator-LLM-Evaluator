import os
os.environ["HF_HOME"] = r"D:\huggingface_cache"
from src.agents.gemini_pipeline import generate_mcq_pipeline as run_gemini
from src.agents.qwen_pipeline import generate_qwen_mcq as run_qwen
from src.eval.judge import evaluate_mcq
from src.eval.logger import log_benchmark_result
from src.rag.retrieval import retrieve_context
import time

def compare_models(topic: str) -> dict:
    results = {"gemini": None, "qwen": None}
    raw_context = retrieve_context(topic, n_results=2)
    
    def _run_g():
        print("\n--- CLOUD MODEL (Gemini 3.5 Flash) ---")
        start_time = time.time()
        try:
            gemini_result, gemini_in, gemini_out = run_gemini(topic)
            gemini_latency = time.time() - start_time
            mcq_json = gemini_result.model_dump_json(indent=2)
            try:
                gemini_scores = evaluate_mcq(topic, raw_context, mcq_json)
            except Exception as judge_err:
                print(f"Judge failed for Gemini: {judge_err}")
                gemini_scores = {"hallucination_score": 0, "logic_score": 0, "plausibility_score": 0, "feedback": f"Judge Error: {judge_err}"}
                
            log_entry = log_benchmark_result(
                model_name="Gemini 3.5 Flash", topic=topic, latency_sec=gemini_latency,
                input_tokens=gemini_in, output_tokens=gemini_out, judge_scores=gemini_scores
            )
            return {"mcq": gemini_result.model_dump(), "log": log_entry}
        except Exception as e:
            print(f"Gemini Pipeline Failed: {e}")
            from src.agents.schemas import FinalMCQ
            fallback_mcq = FinalMCQ(
                question=f"Gemini API Error: {e}",
                option_a="N/A", option_b="N/A", option_c="N/A", option_d="N/A",
                correct_answer="A", explanation="The Cloud API failed to respond."
            )
            log_entry = log_benchmark_result(
                model_name="Gemini 3.5 Flash", topic=topic, latency_sec=0,
                input_tokens=0, output_tokens=0, judge_scores={"hallucination_score": 0, "logic_score": 0, "plausibility_score": 0, "feedback": "Pipeline crashed before judging."}
            )
            return {"mcq": fallback_mcq.model_dump(), "log": log_entry}

    def _run_q():
        print("\n--- LOCAL MODEL (Qwen2.5-0.5B-Instruct on GTX 1650) ---")
        start_time = time.time()
        try:
            qwen_result, qwen_in, qwen_out = run_qwen(topic)
            qwen_latency = time.time() - start_time
            mcq_json = qwen_result.model_dump_json(indent=2)
            try:
                qwen_scores = evaluate_mcq(topic, raw_context, mcq_json)
            except Exception as judge_err:
                print(f"Judge failed for Qwen: {judge_err}")
                qwen_scores = {"hallucination_score": 0, "logic_score": 0, "plausibility_score": 0, "feedback": f"Judge Error: {judge_err}"}
                
            log_entry = log_benchmark_result(
                model_name="Qwen2.5-0.5B-Instruct", topic=topic, latency_sec=qwen_latency,
                input_tokens=qwen_in, output_tokens=qwen_out, judge_scores=qwen_scores
            )
            return {"mcq": qwen_result.model_dump(), "log": log_entry}
        except Exception as e:
            print(f"Qwen Pipeline Failed: {e}")
            from src.agents.schemas import FinalMCQ
            fallback_mcq = FinalMCQ(
                question=f"Qwen Local Error: {e}",
                option_a="N/A", option_b="N/A", option_c="N/A", option_d="N/A",
                correct_answer="A", explanation="The local model ran out of memory or failed."
            )
            log_entry = log_benchmark_result(
                model_name="Qwen2.5-0.5B-Instruct", topic=topic, latency_sec=0,
                input_tokens=0, output_tokens=0, judge_scores={"hallucination_score": 0, "logic_score": 0, "plausibility_score": 0, "feedback": "Pipeline crashed before judging."}
            )
            return {"mcq": fallback_mcq.model_dump(), "log": log_entry}

    import concurrent.futures
    print("Launching Gemini and Qwen concurrently...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future_g = executor.submit(_run_g)
        future_q = executor.submit(_run_q)
        
        results["gemini"] = future_g.result()
        results["qwen"] = future_q.result()

    return results

if __name__ == "__main__":
    compare_models("The Discriminant of a Quadratic Equation")
