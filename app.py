import streamlit as st
import os

from dotenv import load_dotenv
from utils.skill_gap import skill_gap_analysis
from utils.resume_parser import extract_text
from utils.ats_score import calculate_ats_score
from utils.question_generator import generate_questions
from utils.resume_improver import improve_resume

load_dotenv()

# ---------- Custom CSS ----------

st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

.stButton button {
    width: 100%;
    border-radius: 10px;
    height: 50px;
    font-size: 16px;
}

textarea {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------- Header ----------

st.markdown("""
<h1 style='text-align:center; color:#4CAF50;'>
🚀 AI Resume Analyzer
</h1>

<h4 style='text-align:center; color:gray;'>
Optimize Your Resume for ATS and Crack Interviews
</h4>
""", unsafe_allow_html=True)

# ---------- Resume Upload ----------

uploaded_resume = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

# ---------- Job Description ----------

col1, col2 = st.columns([4,1])

with col1:
    jd = st.text_area(
        "Paste Job Description",
        height=250
    )

with col2:
    st.write("")
    st.write("")
    check_jd = st.button("✓ Check JD")

if check_jd:

    if len(jd.strip()) < 100:
        st.warning("Job Description is too short.")

    else:
        st.success("Job Description looks good.")

# ---------- Main Processing ----------

if uploaded_resume and jd:

    resume_text = extract_text(uploaded_resume)

    st.subheader("📝 Resume Editor")

    edited_resume = st.text_area(
        "Edit Resume Content",
        resume_text,
        height=300
    )

    score = calculate_ats_score(
        edited_resume,
        jd
    )

    # ---------- Tabs ----------

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📊 ATS Analysis",
            "📄 Resume Suggestions",
            "🎯 Interview Questions",
            "🧠 Skill Gap Analysis"
        ]
    )

    # ---------- ATS TAB ----------

    with tab1:

        st.subheader("ATS Score")

        st.progress(score / 100)

        st.metric(
            label="Resume Match",
            value=f"{score}%"
        )

    # ---------- RESUME TAB ----------

    with tab2:

        if st.button("Analyze Resume"):

            with st.spinner("Analyzing Resume..."):

                suggestions = improve_resume(
                    edited_resume
                )

            st.subheader("Resume Suggestions")

            st.write(suggestions)

            st.download_button(
                label="📥 Download Suggestions",
                data=suggestions,
                file_name="resume_suggestions.txt",
                mime="text/plain"
            )

    # ---------- QUESTIONS TAB ----------

    with tab3:

        if st.button("Generate Questions"):

            with st.spinner("Generating Questions..."):

                questions = generate_questions(jd)

            st.subheader("Interview Questions")

            st.write(questions)

    # ---------- SKILL GAP TAB ----------

    with tab4:

        if st.button("Analyze Skill Gap"):

            with st.spinner("Analyzing Skills..."):

                result = skill_gap_analysis(
                    edited_resume,
                    jd
                )

            st.subheader("Skill Gap Analysis")

            st.write(result)
