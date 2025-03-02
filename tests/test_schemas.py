import pytest
from assertpy import assert_that
from pydantic import ValidationError
from app.schemas import LLMMessage, QuizOption, QuizQuestion, Quiz

def test_llm_message():
    message = LLMMessage(role="system", content="Test content")
    assert_that(message.role).is_equal_to("system")
    assert_that(message.content).is_equal_to("Test content")

def test_quiz_option():
    option = QuizOption(answer="Test answer", correct=True)
    assert_that(option.answer).is_equal_to("Test answer")
    assert_that(option.correct).is_true()

def test_quiz_question():
    options = [QuizOption(answer="Answer 1", correct=True), QuizOption(answer="Answer 2", correct=False)]
    question = QuizQuestion(question="Test question", options=options)
    assert_that(question.question).is_equal_to("Test question")
    assert_that(question.options).is_length(2)

def test_quiz_question_invalid():
    options = [QuizOption(answer="Answer 1", correct=True), QuizOption(answer="Answer 2", correct=True)]
    with pytest.raises(ValidationError):
        QuizQuestion(question="Test question", options=options)

def test_quiz():
    options = [QuizOption(answer="Answer 1", correct=True), QuizOption(answer="Answer 2", correct=False)]
    questions = [QuizQuestion(question="Test question", options=options)]
    quiz = Quiz(questions=questions)
    assert_that(quiz.questions).is_length(1)
