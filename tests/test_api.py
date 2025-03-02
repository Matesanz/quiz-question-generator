import pytest
from fastapi.testclient import TestClient
from app.api import app_api

client = TestClient(app_api)

def test_health():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() is True

def test_generate_quiz(mocker):
    mock_generate_quiz = mocker.patch('app.quiz_generator.generate_quiz')
    mock_generate_quiz.return_value = {"questions": [{"question": "What is 2+2?", "options": [{"answer": "4", "correct": True}, {"answer": "3", "correct": False}, {"answer": "5", "correct": False}, {"answer": "6", "correct": False}]}]}

    response = client.post("/generate-quiz", json={"learning_objective": "Test Objective", "n_questions": 5})
    assert response.status_code == 200
    assert response.json()["questions"][0]["question"] == "What is 2+2?"
