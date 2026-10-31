from ai.quiz_generator import generate_quiz
import streamlit as st
from dotenv import load_dotenv
from google import genai
import os

from utils.pdf_reader import extract_text_from_pdf
from ai.exam_notes import generate_exam_notes
from ml.predict_time import predict_study_time

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="wide"
)

# -----------------------------
# App Title
# -----------------------------
st.title("📚 StudyMate AI")
st.write("Upload your study notes and let AI help you learn smarter!")

# -----------------------------
# Upload PDF
# -----------------------------
uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)

# -----------------------------
# Main App
# -----------------------------
if uploaded_file is not None:

    st.success(f"✅ File uploaded successfully: {uploaded_file.name}")

    # Extract PDF Text
    text = extract_text_from_pdf(uploaded_file)

    try:

        # -----------------------------
        # AI Exam Ready Notes
        # -----------------------------
        with st.spinner("🤖 Generating Exam-Ready Notes..."):
            exam_notes = generate_exam_notes(client, text)

        st.subheader("📚 AI Exam-Ready Notes")
        st.markdown(exam_notes)

        # -----------------------------
        # Study Time Prediction
        # -----------------------------
        pages = 1
        words = len(text.split())
        topics = exam_notes.count("#")
        difficulty = 2

        study_time = predict_study_time(
            pages,
            words,
            topics,
            difficulty
        )

        st.subheader("⏱ Estimated Study Time")
        st.success(f"📖 Estimated Study Time: {study_time:.2f} Hours")

        # -----------------------------
        # AI Quiz
        # -----------------------------
        st.divider()
        st.subheader("📝 AI Quiz")

        with st.spinner("🤖 Generating Quiz..."):
            quiz = generate_quiz(client, exam_notes)

        for i, question in enumerate(quiz):

            st.write(f"### Question {i+1}")
            st.write(question["question"])

            st.radio(
                "Choose your answer:",
                question["options"],
                key=f"q{i}"
            )

    except Exception as e:
        st.error(f"Error: {e}")