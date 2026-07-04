# Dual-Model MCQ Generator & LLM Evaluator

An automated pipeline that generates multiple-choice questions (MCQs) and distractors from NCERT textbook content using Retrieval-Augmented Generation (RAG). The system features a side-by-side comparative evaluation engine built in Streamlit, pitting a local open-source LLM (Qwen2.5-0.5B-Instruct) against a cloud-based LLM (Gemini).

## Features
- **Multi-Agent RAG Pipeline:** Uses an Educator Agent to generate questions and a Misconception Specialist Agent to engineer highly plausible student distractors.
- **LLM-as-a-Judge Evaluator:** Programmatically scores model outputs on Hallucination, Logic, and Plausibility using **Groq (Llama 3.3 70B)** for ultra-fast, robust evaluation.
- **Dual-Model Benchmarking:** Directly compare a local edge-device model running in `fp16` (Qwen) against a cloud API (Gemini) with real-time latency and token metrics.
- **LaTeX Math Preservation:** Uses Gemini Vision as an OCR pre-processor to ingest textbook PDFs without breaking complex mathematical formulas.

## Architecture
1. **Data Ingestion:** PDFs → Gemini Vision (OCR) → Markdown → Paragraph Chunking → ChromaDB (all-MiniLM-L6-v2 embeddings).
2. **Generation:** Pydantic schemas enforce strict JSON generation for both Local and Cloud execution paths.
3. **Evaluation:** Groq's API (`llama-3.3-70b-versatile`) serves as the LLM-as-a-Judge to score both pipelines simultaneously.
4. **UI Dashboard:** Streamlit frontend allowing real-time topic selection, MCQ display, and performance logging.

## Hardware Optimization
This project was strictly constrained to run on a **GTX 1650 with 4GB VRAM**.
- The `Qwen2.5-0.5B-Instruct` model is loaded locally via HuggingFace `transformers` using `torch.float16`, `device_map="cuda"`, and `attn_implementation="sdpa"` to maximize inference speed and prevent CUDA Out-of-Memory crashes.
- The `HF_HOME` cache is forcibly migrated to a secondary drive to prevent Windows Paging File exhaustion (`os error 1455`) during tensor allocation.

## Setup Instructions
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `.\venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file in the root directory and add your API keys:
   ```env
   GEMINI_API_KEY=your_google_ai_studio_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```
6. Run the Streamlit dashboard:
   ```bash
   streamlit run app/main.py --server.headless true --browser.gatherUsageStats false
   ```

*Note: The first time you run the application, HuggingFace will download the Qwen2.5 model and sentence-transformers to your local cache. Ensure you have at least 2GB of free disk space and enough RAM to load the models.*
