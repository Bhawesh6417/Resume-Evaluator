📄 Resume Evaluator + Interview Question Generator

This is a Streamlit web application that uses Google Gemini 2.0 Flash Exp to evaluate a candidate's resume against a provided job description or tech stack. It also generates relevant technical and behavioral interview questions based on the match.

🚀 Features

Upload a candidate's resume in PDF format

Enter a job description or required skillset

Analyze resume for suitability and skill match

Generate a suitability score (out of 100)

Get a detailed analysis of matched and missing skills

Receive 5 smart interview questions based on the resume and job

Clean and user-friendly interface using Streamlit

🧠 Powered By

Google Gemini 2.0 Flash Exp

Streamlit

PyPDF2

python-dotenv

📦 Setup Instructions

1. Install Dependencies

pip install -r requirements.txt

2. Add API Key in .env

GOOGLE_API_KEY=your_google_api_key

3. Run the Streamlit App

streamlit run resume_checker_app.py

📝 Example Use Cases

Screening candidates based on skillset fit

![image](https://github.com/user-attachments/assets/be98546e-7f6f-47d5-bb0a-3b60dab89559)


Auto-generating interview questions

![image](https://github.com/user-attachments/assets/68220c11-8dc5-4233-bb64-ff06f8e2061f)


📌 Notes

Make sure the resume is in readable PDF format

Model used: gemini-2.0-flash-exp

Internet connection is required
