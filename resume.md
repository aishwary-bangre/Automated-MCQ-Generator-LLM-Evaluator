# Dual-Model MCQ Generator & LLM Evaluator

**Project Overview:**
An automated pipeline that generates multiple-choice questions (MCQs) and distractors from textbook content using Retrieval-Augmented Generation (RAG). The system features a side-by-side comparative evaluation engine built in Streamlit, pitting a local quantized LLM (Qwen2.5-0.5B-Instruct on a GTX 1650) against a cloud-based LLM (Gemini 3.5 Flash).

**Tech Stack:** Python, PyTorch, HuggingFace Transformers, ChromaDB (Vector DB), Google Gemini API, Streamlit, Prompt Engineering, Pydantic, Regex.

---

## Resume Bullet Points

* **Architected a Multi-Agent LLM pipeline** to automatically generate curriculum-aligned educational content (Math MCQs), employing specialized agents for question generation and student-misconception distractor engineering.
* **Built a customized Retrieval-Augmented Generation (RAG) system** using ChromaDB, developing an LLM-aided OCR pipeline to successfully ingest, sanitize, and chunk textbook PDFs containing complex, multi-line LaTeX math formulas.
* **Engineered a Dual-Model Benchmarking Suite** to conduct real-time A/B testing between a cloud API (Gemini 3.5 Flash) and a local open-source model (Qwen2.5-0.5B), tracking telemetry metrics like inference latency, token efficiency, and compute cost.
* **Overcame strict edge-hardware constraints (4GB VRAM, 8GB RAM)** by deploying a 0.5B parameter model locally via HuggingFace `transformers` in fp16, building a custom regex-based output parser to force deterministic, schema-compliant JSON from raw, unstructured text streams.
* **Implemented an "LLM-as-a-Judge" evaluation framework** to programmatically score model outputs on hallucination, logic, and plausibility, enforcing educational integrity.

---

## Technical Challenges & Engineering Solutions

### 1. Handling Unstructured Math Data in RAG
* **Problem:** Traditional PDF parsers (like PyPDF2) completely scramble mathematical formulas — subscripts, superscripts, fractions, and multi-line equations all get mangled into unreadable text. This made standard textbook ingestion impossible for a math-focused generation pipeline.
* **Solution:**
  - Used Gemini as an LLM-aided OCR pre-processor: uploaded the raw NCERT PDF directly to the Gemini Vision API and instructed it to output perfectly formatted LaTeX Markdown.
  - Wrote a smart chunker that split documents by double-newlines (`\n\n`) so that complex multi-line theorems and derivations were never fractured mid-formula before going into the ChromaDB vector store.

### 2. Severe Hardware Constraints & CUDA Out-of-Memory (OOM)
* **Problem:** The initial target model (Qwen2.5-1.5B-Instruct, ~3GB in fp16) repeatedly crashed the PyTorch backend on a GTX 1650 with only 4GB VRAM and 8GB system RAM. The system threw `CUDA Out of Memory` errors during model loading, before even a single token was generated.
* **Solution:**
  - Experimented with `bitsandbytes` 8-bit quantization to squeeze the 1.5B model into VRAM, but abandoned this approach due to inference quality degradation.
  - Pivoted to the highly optimized Qwen2.5-0.5B-Instruct model (~1GB in fp16), which fit comfortably inside the 4GB VRAM ceiling while still producing coherent, instruction-following outputs.
  - Loaded the model with `dtype=torch.float16`, `device_map="auto"`, and `low_cpu_mem_usage=True` to minimize peak memory footprint during weight loading.

### 3. Windows Paging File Exhaustion (OS Error 1455)
* **Problem:** Even after switching to the 0.5B model, running the full dual-model pipeline (Streamlit + ChromaDB + PyTorch + Gemini API) simultaneously caused Windows to run out of virtual memory. The system threw `OSError: The paging file is too small for this operation to complete (os error 1455)`, crashing the entire Python process before PyTorch could even finish loading model weights.
* **Solution:**
  - Diagnosed that with 86% RAM utilization (6.4/7.4 GB), Windows' dynamically managed page file couldn't allocate the contiguous virtual memory block PyTorch needed for `safetensors` memory-mapping.
  - Resolved by closing competing processes before inference runs and keeping the model cached in global Python variables after first load, eliminating repeated allocation/deallocation cycles that fragmented virtual memory.

### 4. C: Drive Storage Exhaustion (17GB → 7GB)
* **Problem:** Over the course of development, the C: drive silently lost 10GB of free space. Investigation revealed that HuggingFace model downloads (`~/.cache/huggingface`), pip package caches, and Windows temp files were all defaulting to the C: drive, which had limited capacity.
* **Solution:**
  - Redirected the HuggingFace cache to the secondary D: drive by setting `HF_HOME=D:\huggingface_cache` as an environment variable at the top of every script that imports `transformers` or `sentence-transformers`.
  - Purged ~6GB of accumulated temporary caches (HuggingFace hub cache, pip download cache, Windows `%TEMP%` files) to reclaim C: drive space.
  - Updated the `.env` file to persist this configuration across all sessions.

### 5. Forcing Structured JSON from Small Open-Source Models
* **Problem:** While cloud APIs like Gemini have built-in JSON mode (`response_mime_type="application/json"`), local models have no such guarantee. The 0.5B Qwen model aggressively inserted LaTeX escape characters (`\(`, `\)`, `\[`, `\]`) inside its generated strings, which immediately crashed standard `json.loads()` parsing — even when the JSON structure was otherwise valid.
* **Solution:**
  - Implemented strict few-shot prompting with explicit "no LaTeX, no markdown" system instructions.
  - Engineered a custom multi-stage JSON extraction function:
    1. Pre-sanitize the raw text by stripping LaTeX backslash patterns before parsing.
    2. Use brace-depth counting to extract the first valid JSON object from arbitrary text (handling cases where the model prepends/appends conversational filler).
    3. Fallback to partial JSON repair for truncated outputs (finding the last valid `}` and attempting parse).
  - Validated all extracted JSON against Pydantic schemas (`EducatorOutput`, `SpecialistOutput`, `FinalMCQ`) to enforce strict type safety.

### 6. Aggressive Cloud API Rate Limiting (429 RESOURCE_EXHAUSTED)
* **Problem:** The Gemini free-tier API enforces a strict 20-request-per-day quota per model. During development and testing, this quota was quickly exhausted, causing both the Gemini MCQ pipeline AND the LLM-as-a-Judge evaluator to fail with `429 RESOURCE_EXHAUSTED` errors — which cascaded to make the Qwen pipeline also appear "failed" (since its output couldn't be scored).
* **Solution:**
  - Discovered that Google tracks rate limits per-model, not per-API-key. Queried the available models list via `client.models.list()` and migrated from `gemini-2.5-flash` to `gemini-3.5-flash`, which had its own completely fresh quota bucket.
  - Architected the orchestrator with independent try/except blocks so that if one model's pipeline fails (e.g., Gemini hits rate limit), the other model's results are still returned and displayed on the dashboard.

### 7. API Model Deprecation & 404 Errors
* **Problem:** After switching from `gemini-2.5-flash` to `gemini-1.5-flash` to dodge rate limits, the API returned `404 NOT_FOUND: models/gemini-1.5-flash is not found for API version v1beta`. Google had silently deprecated older model versions from the latest API endpoints.
* **Solution:**
  - Programmatically queried the live model registry (`client.models.list()`) to discover all currently supported model identifiers.
  - Identified `gemini-3.5-flash` as the correct, actively supported model and updated all pipeline references across the codebase.

### 8. PyTorch Security Block (CVE-2025-32434)
* **Problem:** PyTorch 2.5+ introduced a security patch that blocks `torch.load()` with `weights_only=False` by default, to prevent arbitrary code execution from untrusted model files. This caused HuggingFace's `from_pretrained()` to fail when loading the Qwen model weights, even though the model was from a trusted source.
* **Solution:**
  - Set the environment variable `TORCH_FORCE_WEIGHTS_ONLY_WARN_ONLY=1` at the top of the pipeline script, which downgrades the hard block to a warning for trusted HuggingFace models while maintaining security awareness.

### 9. Streamlit First-Run Terminal Block
* **Problem:** When launching Streamlit for the first time on a machine, it pauses the entire terminal process and prompts the user to enter an email address for their mailing list. This caused the web server to never actually start — the browser showed a blank/black screen, and closing the terminal triggered a `ConnectionResetError: [WinError 10054]`.
* **Solution:**
  - Launched Streamlit with `--server.headless true` and `--browser.gatherUsageStats false` flags to bypass all interactive prompts.
  - Created a global Streamlit credentials file (`~/.streamlit/credentials.toml`) to permanently suppress the email prompt on subsequent launches.

### 10. Deep Module Caching & Hot-Reload Failures
* **Problem:** After fixing environment variables (like API keys) or updating model configuration strings in backend files, the Streamlit UI continued throwing the old errors. Changes seemed to have no effect.
* **Solution:**
  - Identified that Streamlit's hot-reload mechanism only re-executes the entry script (`main.py`) but does NOT reload deeply nested imports (`orchestrator.py`, `gemini_pipeline.py`, `judge.py`). Python's `sys.modules` cache keeps the old module objects alive in memory.
  - Implemented hard-reboot protocols: fully stopping and restarting the Streamlit server process to flush all cached modules and force fresh imports with the updated configurations.

### 11. Accidental Codebase Wipe from Faulty Batch Script
* **Problem:** While attempting to batch-rename all Gemini model references across the codebase (e.g., swapping `gemini-2.5-flash` → `gemini-1.5-flash`), a Python one-liner script had a fatal execution-order bug. The list comprehension `[open(f, 'w').write(open(f, 'r').read().replace(...)) for f in files]` opened each file for writing (truncating it to 0 bytes) *before* the inner `open(f, 'r').read()` could read the original content. This silently wiped 7 critical project files — including `gemini_pipeline.py`, `orchestrator.py`, `judge.py`, `main.py`, `resume.md`, and `implementation-plan.md` — down to empty files with zero bytes.
* **Solution:**
  - Since the project had no Git version control initialized at that point, there was no `git checkout` recovery option available.
  - Attempted to recover files from Cursor IDE's local history and from the AI agent's conversation transcript logs, but both sources were unavailable (local history didn't track those files, and the transcript folder had been relocated).
  - Ultimately rebuilt all 7 files from scratch by referencing the architectural knowledge accumulated during development — a painful but effective recovery.
  - **Lesson learned:** Always initialize `git init` and make frequent commits from Day 1, even for experimental projects. A single `git checkout -- .` would have recovered everything instantly.

### 12. Model Migration: Falcon vs. Qwen (Structured Output Failure)
* **Problem:** The local pipeline was initially built using a small Falcon model. However, Falcon severely struggled with instruction-following for structured outputs. Even with strict prompting, it repeatedly hallucinated, ignored the JSON schema, and failed to generate valid Distractor/Misconception JSON pairs. It also lacked the necessary mathematical reasoning capabilities for NCERT-level algebra, rendering the local evaluation pipeline useless.
* **Solution:**
  - Conducted an architectural pivot to replace Falcon with **Qwen2.5-0.5B-Instruct**.
  - Qwen2.5 proved vastly superior at following complex JSON schemas and system prompts despite being only 0.5B parameters. It provided the perfect balance of logical reasoning and strict formatting while still fitting inside the extreme 4GB VRAM constraint.
  - This migration solved the persistent JSON parsing crashes and dramatically improved the LLM-as-a-Judge scores on the local pipeline.

### 13. GPU VRAM Leak in Long-Running Streamlit Server
* **Problem:** Moving from short-lived test scripts (`test_run.py`) to a persistent Streamlit web server caused the Qwen model to permanently lock ~1GB of VRAM. The PyTorch model and tokenizer remained cached in Python global variables (`model`, `tokenizer` in `qwen_pipeline.py`), keeping the GPU's 3D utilization spiking to 100% during generation while the 4GB VRAM stayed partially occupied even when idle.
* **Solution:**
  - Made a deliberate architectural trade-off: rather than aggressively calling `torch.cuda.empty_cache()` and deleting the model after every generation (which would add a 5–10 second cold-start penalty for each subsequent request), the model was intentionally kept cached in global memory.
  - This ensured instant responsiveness for the end-user when generating back-to-back questions, at the cost of ~1GB of permanently reserved VRAM — an acceptable trade-off given the 4GB budget.

### 14. Embedding Model Cache Path Mismatch
* **Problem:** ChromaDB's `SentenceTransformerEmbeddingFunction` (using `all-MiniLM-L6-v2`) defaults to downloading/loading models from `C:\Users\<user>\.cache\huggingface`. While the Qwen model path was explicitly redirected to D: drive via `HF_HOME`, the `retrieval.py` script imported ChromaDB *before* the environment variable was set, causing the embedding function to silently search the wrong cache directory and hang indefinitely during model loading.
* **Solution:**
  - Moved `os.environ["HF_HOME"] = r"D:\huggingface_cache"` to the very top of `retrieval.py`, before any `import chromadb` statement, ensuring the environment variable is set before any HuggingFace-dependent library initializes its cache path.

---

## Interview Talking Points / "The Story Behind the Code"

### The Architecture
The system uses a **Multi-Agent RAG pipeline** with three distinct layers:
1. **RAG Layer**: NCERT Math PDFs → Gemini OCR → Markdown → Paragraph Chunking → ChromaDB Vector Store → Semantic Retrieval via `all-MiniLM-L6-v2` embeddings.
2. **Generation Layer**: Two specialized agents (Educator + Misconception Specialist) run independently on both Qwen (local GPU) and Gemini (cloud API), producing structured MCQs with Pydantic-validated schemas.
3. **Evaluation Layer**: An LLM-as-a-Judge scores each model's output on Hallucination (0–10), Logic (0–10), and Plausibility (0–10), enabling quantitative comparison of open-source vs. proprietary models.

### Key Metrics
| Metric | Qwen2.5-0.5B (Local) | Gemini 3.5 Flash (Cloud) |
|--------|----------------------|--------------------------|
| Inference Latency | ~30-35s | ~5-10s |
| Cost per Question | $0.00 | ~$0.0001 |
| VRAM Usage | ~1GB (fp16) | N/A (API) |
| Judge Score (avg) | 6-8/10 | 9-10/10 |

---

## Interview Q&A Preparation

### 1. How is "Qwen" pronounced, and what is its origin?
* **Pronunciation:** "Ch-wen" (like the *ch* in "cheese" + *when*).
* **Origin:** Created by Alibaba Cloud, it is a leading open-source family of models (Tongyi Qianwen).

### 2. Why did you choose Qwen2.5-0.5B-Instruct instead of a larger model?
* **VRAM Bottleneck:** Our edge hardware constraint was a 4GB VRAM GPU. A 1.5B model in float16 takes ~3GB, which doesn't leave enough room for context tokens and KV cache. The 0.5B model takes exactly **1.0 GB** of VRAM, running extremely fast and avoiding Out-of-Memory crashes.
* **JSON Compliance:** Standard small models struggle with JSON, but Qwen's Instruct variant is fine-tuned to follow formatting prompts reliably.
* **Math Logic:** In the sub-1B category, Qwen2.5 outperforms competitor architectures (like Falcon or old Llama models) in logical and mathematical reasoning.

### 3. What is an LPU, and why is it faster than a GPU for LLMs?
* **LPU (Language Processing Unit):** A custom computer chip designed by Groq specifically for processing sequential language models.
* **The Difference:** Traditional GPUs are bottlenecked by memory transfer speeds (reading weights from **VRAM** to compute cores). Groq's LPU stores the AI model entirely in **SRAM** (Static RAM) which is physically integrated next to the compute cores. This completely eliminates the data-transfer delay, letting Llama 3 run at **800+ tokens per second** (compared to 100-200 t/s on cloud GPUs/TPUs).

### 4. What is the difference between SRAM and VRAM?
* **VRAM (Video RAM):** Large memory pool soldered onto a GPU board (like our 4GB GTX 1650). It holds massive models but has slower transfer rates.
* **SRAM (Static RAM):** Microscopic, ultra-fast memory placed directly inside the processor silicon. It is extremely expensive and small, but has near-zero latency.

### 5. Why would running Qwen on the CPU/System RAM be significantly slower, even with a RAM upgrade?
* **Core Architecture:** A CPU has a few very fast cores (4 to 8) that run calculations sequentially. A GPU has hundreds or thousands of parallel cores (our GTX 1650 has 896 CUDA cores) designed to run matrix multiplications simultaneously.
* **Memory Bandwidth:** Standard DDR4 RAM has a bandwidth of ~25-48 GB/s. GDDR6 VRAM on the GPU runs at **128 GB/s**—transferring model weights to the compute cores 3 to 4 times faster.

### 6. What are CUDA and SDPA, and how do they prevent OOM?
* **CUDA (Compute Unified Device Architecture):** Nvidia's platform that allows PyTorch to bypass the CPU and run code directly on GPU cores.
* **SDPA (Scaled Dot Product Attention):** An optimized attention algorithm in PyTorch 2.x.
* **OOM Prevention:** Standard attention calculations grow quadratically ($O(N^2)$) relative to text length, causing massive VRAM spikes. SDPA uses **tiling** to process text in small blocks, reducing memory growth to linear ($O(N)$) and keeping the VRAM footprint flat.

### 7. Why did you write a custom JSON sanitizer for Qwen?
* Tiny models (0.5B) often hallucinate syntax errors (like single quotes instead of double quotes, or escaping LaTeX backslashes incorrectly). A single bad backslash crashes Python's standard `json.loads()`.
* The sanitizer uses regex to isolate the `{...}` block and replaces single backslashes `\` with double backslashes `\\` so Python parses it cleanly, with an AST (Abstract Syntax Tree) parsing fallback if it still fails.

### 8. What does `sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))` do?
* In Python, files cannot import modules from folders outside or above their current directory.
* This command finds the directory of the current file (`app/main.py`), goes up one directory level (`..`), gets the absolute path to the root folder, and appends it to Python's system search path (`sys.path`). This lets `app/main.py` import files from the `src/` directory.

