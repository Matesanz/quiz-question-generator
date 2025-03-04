"""Streamlit UI for the Quiz Question Generator application.

Can be run with `streamlit run app/ui.py`.
Used only for demo purposes.
Code quality is not a priority.
"""
# pylint: skip-file
# ruff: noqa
import os
import time

import requests
import streamlit as st

API_CONNECTION_ATTEMPS = os.getenv("API_CONNECTION_ATTEMPS", 1)
WAIT_BETWEEN_RETRIES  = os.getenv("WAIT_BETWEEN_RETRIES", 5)
API_TIMEOUT = os.getenv("API_TIMEOUT", 10)
API_URL = os.getenv("API_URL", "http://localhost:8000")
QUIZ_CREATION_URL = f"{API_URL}/generate-quiz"

def wait_for_api() -> bool:
    for _ in range(API_CONNECTION_ATTEMPS):
        try:
            response = requests.get(API_URL, timeout=API_TIMEOUT)
            if response.status_code == 200:
                return True
        except requests.RequestException:
            pass # ignore and retry
        time.sleep(WAIT_BETWEEN_RETRIES)
    
    st.error(f"Failed to connect to the API at {API_URL}. Please try again later.")
    st.stop()
    return False
        
def set_config():
    st.set_page_config(
        page_title="Quizz App Generator",
        page_icon="❓",
    )

def initialize():
    set_config()
    with st.spinner("Connecting to the Backend..."):
        wait_for_api()

def retrieve_quiz(learning_objective: str, n_questions: int) -> dict:
    body = {"learning_objective": learning_objective, "n_questions": n_questions}
    response = requests.post(QUIZ_CREATION_URL, json=body)
    response.raise_for_status()
    return response.json()

def save_quiz(quiz: dict):
    st.session_state.quiz = quiz

def load_quiz():
    return st.session_state.get("quiz", None)

def save_learning_objective(learning_objective: str):
    st.session_state.learning_objective = learning_objective

def load_learning_objective():
    return st.session_state.get("learning_objective", None)

def display_quiz_question(quiz_question: dict):

    question = quiz_question["question"]
    options = quiz_question["options"]

    def _display_question():
        st.markdown("---")
        st.subheader(question)

    def _display_options() -> str:
        answers = [option["answer"] for option in options]
        return st.radio("Select an answer", answers)

    def _handle_question_submission(selected_answer: str):
        correct_answer = next((option["answer"] for option in options if option["correct"]), None)
        if st.button("Submit", key=question, use_container_width=True, type="secondary"):
            if selected_answer == correct_answer:
                st.success("🎉 Correct!")
            else:
                st.error(f"❌ Incorrect! The correct answer is: {correct_answer}")

    _display_question()
    selected_answer = _display_options()
    _handle_question_submission(selected_answer)

def display_sidebar():
    st.sidebar.title("Generate a new quiz")
    learning_objective = st.sidebar.text_input("Learning Objective", help="Enter the learning objective for the quiz")
    n_questions = st.sidebar.number_input("Number of Questions", min_value=1, value=2, help="Enter the number of questions to include in the quiz")
    if st.sidebar.button("Generate Quiz", key="generate_quiz", use_container_width=True, type="primary", disabled=not learning_objective):
        with st.spinner(f"Generating quiz about '{learning_objective}'..."):
            quiz = retrieve_quiz(learning_objective, n_questions)
        save_quiz(quiz)
        save_learning_objective(learning_objective)

def display_info():
    st.title("Quiz Question Generator")
    st.info("👈 No quiz loaded. Use the sidebar to generate a new quiz.")

def display_quiz(quiz: dict):
    learning_objective = load_learning_objective()
    st.title(f"Quiz on {learning_objective}")
    st.success(f"🎉 A new quiz was generated based on the learning objective: **'{learning_objective}'**")
    questions = quiz["questions"]
    for question in questions:
        display_quiz_question(question)

def run():
    display_sidebar()
    quiz = load_quiz()
    if quiz:
        display_quiz(quiz)
    else:
        display_info()

initialize()
run()
