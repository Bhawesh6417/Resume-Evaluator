import streamlit as st
import google.generativeai as genai
from google.generativeai import GenerativeModel
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os

# Load environment variable
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
else:
    st.error("GOOGLE_API_KEY not found in environment variables.")

# Initialize Gemini model
model = GenerativeModel("gemini-2.0-flash-exp")

# Streamlit UI
st.set_page_config(page_title="Resume Suitability & Interview Prep", layout="wide")
st.title("📄 Resume Evaluator + Interview Question Generator 🤖")
st.markdown("Powered by Gemini 2.0 Flash Exp")

# Upload resume
resume_file = st.file_uploader("📤 Upload Resume (PDF)", type=["pdf"])

# Input job description or tech stack
job_description = st.text_area("🛠️ Enter Job Description / Required Tech Stack", height=200)

if resume_file and job_description:
    # Extract text from resume
    pdf = PdfReader(resume_file)
    resume_text = ""
    for page in pdf.pages:
        resume_text += page.extract_text() or ""

    with st.spinner("Analyzing resume with Gemini..."):
        # Gemini prompt
        suitability_prompt = f"""
        You are a technical recruiter. Analyze the following resume against the job description.

        --- Job Description ---
        {job_description}

        --- Candidate Resume ---
        {resume_text}

        1. Evaluate how well the candidate matches the job requirements.
        2. Highlight matching and missing skills.
        3. Provide a suitability score out of 100.
        4. Give a brief explanation (3-4 bullet points).
        """

        interview_prompt = f"""
        Based on the following job description and candidate resume, generate 5 relevant technical or behavioral interview questions:

        --- Job Description ---
        {job_description}

        --- Candidate Resume ---
        {resume_text}
        """

        # Run Gemini analysis
        suitability_response = model.generate_content(suitability_prompt)
        interview_response = model.generate_content(interview_prompt)

        # Display Results
        st.subheader("✅ Candidate Suitability Evaluation")
        st.markdown(suitability_response.text)

        st.subheader("🎯 Suggested Interview Questions")
        st.markdown(interview_response.text)

elif not resume_file:
    st.info("Please upload a resume.")
elif not job_description:
    st.info("Please enter the job description or tech stack.")

# Style
st.markdown("""
    <style>
    textarea {
        font-size: 16px;
    }
    .stTextArea textarea {
        height: 180px !important;
    }
    </style>
""", unsafe_allow_html=True)
