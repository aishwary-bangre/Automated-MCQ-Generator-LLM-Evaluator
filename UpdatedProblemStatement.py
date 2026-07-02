# Define the content for the problem statement
problem_statement = """
# Project Problem Statement: AI-Powered Benchmarking & Content Generation Dashboard

## 1. Overview
The objective is to build an interactive, Streamlit-based web application that serves as a Dual-Model Benchmarking Engine and an AI-assisted Math MCQ Generator. This platform allows users to compare the performance and output quality of a local open-source LLM (Qwen2.5-0.5B-Instruct) versus a commercial cloud LLM (Gemini 3.5 Flash) in real-time.

## 2. Core Objectives
* **Benchmarking Performance:** Evaluate and compare LLMs based on inference latency, token efficiency, and AI-judged accuracy scores.
* **Content Generation:** Generate high-quality educational content (Math MCQs) grounded in official NCERT textbook documents.
* **Interactive Evaluation:** Provide a user-friendly UI for end-users to interact with the generated content and directly compare local vs cloud generation side-by-side.

## 3. Architecture & Pipeline
### A. Data Ingestion & Retrieval (RAG)
* **Document Processing:** Parse NCERT Math PDFs using Gemini Vision to preserve complex LaTeX formulas, then chunk by paragraphs.
* **Vector Storage:** Store embeddings (via all-MiniLM-L6-v2) in a local ChromaDB instance to allow semantic search.
* **Retrieval:** Upon user query, perform semantic search to retrieve the most relevant textbook context.

### B. Dual-Model Execution Engine
* **Parallel Pipelines:** Two independent pipelines for Qwen2.5-0.5B (Local GPU, HuggingFace) and Gemini 3.5 Flash (Cloud, Google GenAI SDK).
* **Agentic Workflow:** Each model acts as two specialized agents to generate:
    * Agent 1 (Educator): One Question + Correct Answer + Step-by-step Explanation.
    * Agent 2 (Specialist): Three distractor options based on common student misconceptions.
* **Structured Output:** Enforce strict JSON output through system prompting and regex sanitizers to handle faulty escape characters from the local model.

### C. Benchmarking Suite
* **Metrics Collection:** Record inference latency (seconds) and token usage per generation.
* **Evaluation:**    - **LLM-as-a-Judge Evaluator (Groq - Llama 3.3 70B)**: Scores generated MCQs across three dimensions: Hallucination (1-10), Logic (1-10), and Plausibility of Distractors (1-10).
    - **Metrics Tracked**: Generation Latency, Input/Output Token Count, Overall Quality Score.

## 4. User Interface (Streamlit Dashboard)
* **Syllabus Mapper:** User selects the overarching math chapter and a highly specific sub-topic to generate questions for.
* **Interactive MCQ Interface:** Display generated MCQs side-by-side (Local vs Cloud). Allow users to select options and expand explanations.
* **Performance Dashboard:** Visual metrics displaying latency, hardware tokens, and LLM-as-a-Judge evaluation scores.

## 5. Success Criteria & Constraints
* **Hardware Constraints:** The local model (Qwen2.5-0.5B) must successfully run within the tight memory footprint of a 4GB VRAM GPU (GTX 1650).
* **Production Integrity:** 0% hallucination rate enforced by strictly anchoring generation to the retrieved textbook context.
* **Usability:** A clean, intuitive dashboard that allows non-technical users to generate, test, and evaluate AI educational content seamlessly.
"""

# Save to a file
file_path = "Project_Problem_Statement.txt"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(problem_statement)

print(f"File created successfully: {file_path}")