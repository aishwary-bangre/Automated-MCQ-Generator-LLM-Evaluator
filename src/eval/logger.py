import json
import os
from datetime import datetime

LOG_DIR = os.path.join("data", "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "benchmark_results.json")

def log_benchmark_result(
    model_name: str,
    topic: str,
    latency_sec: float,
    input_tokens: int,
    output_tokens: int,
    judge_scores: dict
):
    """
    Logs the benchmark results to a structured JSON file.
    """
    # Simple cost estimation (Gemini 2.5 flash costs roughly $0.075 / 1M input, $0.30 / 1M output)
    # Local model cost is $0.
    cost = 0.0
    if "Gemini" in model_name:
        cost = (input_tokens / 1_000_000 * 0.075) + (output_tokens / 1_000_000 * 0.30)
        
    entry = {
        "timestamp": datetime.now().isoformat(),
        "model": model_name,
        "topic": topic,
        "latency_sec": round(latency_sec, 2),
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "estimated_cost_usd": round(cost, 6),
        "scores": judge_scores
    }
    
    data = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                data = json.load(f)
        except:
            pass
            
    data.append(entry)
    
    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=4)
        
    return entry
