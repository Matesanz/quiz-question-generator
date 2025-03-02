"""FastAPI application for the Quiz Question Generator API."""
from fastapi import FastAPI, HTTPException

from app import __version__, app_config, logs, quiz_generator, schemas

app_api = FastAPI(
    version=__version__,
    debug=app_config.API_DEBUG,
    title="Quiz Question Generator API",
    description="LLM powered API that generates quiz questions based on a learning objective.",
)

@app_api.get("/")
def health() -> bool:
    """Health check endpoint."""
    return True

@app_api.post("/generate-quiz")
def generate_quiz(request: schemas.QuizRequest) -> schemas.Quiz:
    """Generate a Quiz.

    This endpoint uses an LLMs to generate a quiz based on the
    provided learning objective and number of questions.
    """
    try:
        logs.INFO(f"Generating quiz for learning objective: {request.learning_objective}")
        return quiz_generator.generate_quiz(request.learning_objective, request.n_questions)
    except Exception as e:
        logs.ERROR(f"Failed to generate quiz for learning objective: {request.learning_objective}")
        raise HTTPException(status_code=500, detail=str(e)) from e
