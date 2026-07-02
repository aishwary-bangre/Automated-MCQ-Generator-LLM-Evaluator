import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.rag.syllabus_mapper import get_chapters, get_subtopics
from src.agents.orchestrator import compare_models

st.set_page_config(page_title="Dual-Model MCQ Generator", layout="wide")

st.title("📚 Dual-Model MCQ Generator & Evaluator")
st.markdown("Compare a local **Qwen2.5-0.5B** model against the cloud-based **Gemini Flash**.")

with st.sidebar:
    st.header("Syllabus Mapper")
    chapters = get_chapters()
    selected_chapter = st.selectbox("Select Chapter", chapters)
    subtopics = get_subtopics(selected_chapter)
    selected_topic = st.selectbox("Select Sub-Topic", subtopics)
    generate_btn = st.button("Generate Question", type="primary")

if generate_btn:
    with st.spinner(f"Generating question for: {selected_topic}..."):
        results = compare_models(selected_topic)
        if not results["gemini"] and not results["qwen"]:
            st.error("Both models failed to generate a response.")
            st.stop()
            
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Local Model (Qwen2.5-0.5B)")
            if results["qwen"]:
                mcq = results["qwen"]["mcq"]
                log = results["qwen"]["log"]
                st.markdown(f"**Latency**: {log['latency_sec']}s | **Tokens**: {log['input_tokens']} in, {log['output_tokens']} out")
                st.info(f"**Q:** {mcq['question']}")
                for i, opt in enumerate([mcq['option_a'], mcq['option_b'], mcq['option_c'], mcq['option_d']]):
                    st.write(f"{chr(65+i)}) {opt}")
                with st.expander("Show Explanation & Correct Answer"):
                    st.success(f"**Correct Answer:** {mcq['correct_answer']}")
                    st.write(mcq['explanation'])
                st.divider()
                st.markdown("#### LLM-as-a-Judge Scores")
                st.metric("Hallucination (Target 10)", log["scores"].get('hallucination_score', 0))
                st.metric("Logic", log["scores"].get('logic_score', 0))
                st.metric("Plausibility", log["scores"].get('plausibility_score', 0))
                st.write(f"**Feedback**: {log['scores'].get('feedback', '')}")
            else:
                st.error("Qwen pipeline failed.")

        with col2:
            st.subheader("Cloud Model (Gemini Flash)")
            if results["gemini"]:
                mcq = results["gemini"]["mcq"]
                log = results["gemini"]["log"]
                st.markdown(f"**Latency**: {log['latency_sec']}s | **Tokens**: {log['input_tokens']} in, {log['output_tokens']} out")
                st.info(f"**Q:** {mcq['question']}")
                for i, opt in enumerate([mcq['option_a'], mcq['option_b'], mcq['option_c'], mcq['option_d']]):
                    st.write(f"{chr(65+i)}) {opt}")
                with st.expander("Show Explanation & Correct Answer"):
                    st.success(f"**Correct Answer:** {mcq['correct_answer']}")
                    st.write(mcq['explanation'])
                st.divider()
                st.markdown("#### LLM-as-a-Judge Scores")
                st.metric("Hallucination (Target 10)", log["scores"].get('hallucination_score', 0))
                st.metric("Logic", log["scores"].get('logic_score', 0))
                st.metric("Plausibility", log["scores"].get('plausibility_score', 0))
                st.write(f"**Feedback**: {log['scores'].get('feedback', '')}")
            else:
                st.error("Gemini pipeline failed.")
