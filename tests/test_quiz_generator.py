import pytest
from assertpy import assert_that
from app.quiz_generator import compute_quiz_messages, parse_quiz_from_llm_response, generate_quiz
from app.schemas import Quiz

@pytest.fixture
def sample_llm_response():
    return '{"questions": [{"question": "What is 2+2?", "options": [{"answer": "4", "correct": true}, {"answer": "3", "correct": false}, {"answer": "5", "correct": false}, {"answer": "6", "correct": false}]}]}'

def _assert_quiz_has_n_questions(quiz: Quiz, n_questions: int):
    assert_that(quiz.questions).is_length(n_questions)

def _assert_quiz_question_is(quiz: Quiz, question: str):
    assert_that(quiz.questions[0].question).is_equal_to(question)

def test_compute_quiz_messages():
    learning_objective = "Test Objective"
    n_questions = 5
    messages = compute_quiz_messages(learning_objective, n_questions)
    assert_that(messages).is_length(2)
    assert_that(messages[1]['content']).contains(learning_objective)

def test_generate_quiz(mocker, sample_llm_response):
    mock_call_llm = mocker.patch('app.quiz_generator.llm.call_llm')
    mock_call_llm.return_value = sample_llm_response

    learning_objective = "Test Objective"
    n_questions = 1
    quiz = generate_quiz(learning_objective, n_questions)
    _assert_quiz_has_n_questions(quiz, n_questions)
    _assert_quiz_question_is(quiz, "What is 2+2?")
