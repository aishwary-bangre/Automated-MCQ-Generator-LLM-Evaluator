# Project Context: AI-Powered Benchmarking & Content Generation Dashboard

## Overview
The objective is to build an interactive, Streamlit-based web application that serves as a Dual-Model Benchmarking Engine and an AI-assisted Math MCQ Generator. This platform allows users to compare the performance and output quality of a local open-source LLM (Qwen2.5-0.5B-Instruct) versus a commercial cloud LLM (Gemini 2.5 Flash) in real-time. The system leverages Retrieval-Augmented Generation (RAG) to anchor questions in official textbook chapters and utilizes a multi-agent framework to engineer realistic diagnostic distractors based on student misconceptions.

## Core Objectives
- **Benchmarking Performance:** Evaluate and compare LLMs based on inference latency, token efficiency, and AI-judged accuracy scores.
- **Content Generation:** Generate high-quality educational content (Math MCQs) grounded in official NCERT textbook documents.
- **Interactive Evaluation:** Provide a user-friendly UI for end-users to interact with the generated content and provide feedback.

## Scope of Work

### 1. Target Curriculum & Local RAG Module
- **Target Scope:** Class 10 Mathematics (Chapters: Quadratic Equations, Arithmetic Progressions, Coordinate Geometry, Probability).
  - Utilize an LLM-Aided OCR pipeline (Gemini 2.5 Flash) to parse raw textbook PDFs into pristine, full-length LaTeX Markdown files, preserving all complex mathematical notation.
  - Implement a smart paragraph-based chunking strategy to ensure that LaTeX formulas and multi-step word problems are never split in half during vectorization.
  - Generate vector embeddings from these Markdown chunks and store them in a local ChromaDB instance.
- Implement semantic search to retrieve relevant mathematical formulas and concepts based on user-selected topics.

### 2. Multi-Agent Generation Framework
- **Agent 1 (The Educator):** Consumes the retrieved curriculum text from ChromaDB and generates a clear, structurally sound math question along with the correct answer.
- **Agent 2 (The Student Misconception Specialist):** Analyzes the correct question/answer pair and generates exactly three logical incorrect options (distractors) modeled on verified student errors (e.g., sign errors in discriminant, nth term formula mix-ups, order of operations confusion).
- **Output:** Enforce structured output formatting using Pydantic schemas to ensure both LLMs strictly output clean JSON (Question, Options A/B/C/D, Correct Answer, Diagnostic Explanation).
- **LaTeX Sanitization**: Small local models tend to output `\(` which breaks standard JSON parsing. A custom parser sanitizes the output string before attempting to decode the JSON.

### 3. Dual-Model Execution & Benchmarking Suite
- **Execution Paths:** Route the generation topic to run on two parallel execution paths, with *both* Agent 1 and Agent 2 executing natively on their respective models:
  - **Local Execution Pipeline:** Qwen2.5-0.5B-Instruct (loaded via HuggingFace in fp16) generates the question (Agent 1) and its distractors (Agent 2).
  - **Cloud API Execution Pipeline:** Gemini 2.5 Flash (via Google AI Studio) generates the question (Agent 1) and its distractors (Agent 2).
- **Benchmarking Suite:** Build an evaluation script that programmatically records:
  - **Inference Latency:** Total execution time per generation (seconds).
  - **Token Efficiency:** Compute input/output token counts and map estimated dollar costs.
  - **Quality/Accuracy Score:** Run an "LLM-as-a-judge" prompt using Gemini 2.5 Flash to evaluate whether the generated questions match the retrieved curriculum context and if the distractors represent valid conceptual errors.

### 4. User Interface (Streamlit Dashboard)
- **Input Section:** User selects a math topic and the number of questions.
- **Interactive MCQ Interface:** Display generated MCQs side-by-side or sequentially for user interaction.
- **Performance Dashboard:** Visual charts comparing latency, cost, and accuracy scores between models.
- **Feedback Loop:** Allow users to flag incorrect or poor-quality content directly in the UI.

## Success Criteria
- **Production Integrity:** 0% hallucination rate validated by post-inference checks.
- **Technical Performance:** p95 latency under 3 seconds for RAG retrieval and generation.
- **Usability:** A clean, intuitive dashboard that allows non-technical users to generate, test, and evaluate AI-generated educational content.

## Constraints
- **No Paid APIs Required:** The system must run entirely on local compute (Qwen2.5-0.5B) and free-tier developer API keys (Gemini AI Studio).
- **Deterministic Schemas:** The LLM outputs must be strictly parsed; any malformed JSON generation must trigger an automatic retry or graceful fallback.
- **Frameworks:** Built strictly using Python, Streamlit, ChromaDB, HuggingFace transformers, and the Google GenAI SDK.
