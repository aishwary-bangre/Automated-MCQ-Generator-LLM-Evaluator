from src.agents.orchestrator import compare_models

if __name__ == "__main__":
    print("Running orchestrator test to catch exact Gemini Exception...")
    try:
        results = compare_models("Probability")
        print("Test Complete.")
    except Exception as e:
        import traceback
        traceback.print_exc()
