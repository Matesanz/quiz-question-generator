"""Pydantic models for the Quiz Question Generator API."""
from typing import Literal

from pydantic import BaseModel, Field, field_validator


class LLMMessage(BaseModel):
    """Model representing a message for the LLM."""
    role: Literal["system", "user"] = Field(..., description="The role of the message.")
    content: str = Field(..., description="The content of the message for the LLM.")

class QuizOption(BaseModel):
    """Model representing an option for a quiz question."""
    answer: str = Field(..., description="The answer in properly formatted English in a human-readable form")
    correct: bool = Field(..., description="Whether the answer is correct or not")

class QuizQuestion(BaseModel):
    """Model representing a quiz question.

    This model enforces that there is only one correct answer.
    """
    question: str = Field(..., description="The question in properly formatted English in a human-readable form")
    options: list[QuizOption]

    # validate at least one answer is correct
    @field_validator("options")
    def only_one_correct_option(cls, options: list[QuizOption]) -> list[QuizOption]:  # pylint: disable=no-self-argument
        """Validate that there is only one correct option."""
        n_correct_options = sum(option.correct for option in options)
        there_is_only_one_correct_option = n_correct_options == 1
        if there_is_only_one_correct_option:
            return options
        raise ValueError(f"Just one answer has to be correct. Found {n_correct_options} correct options.")

class Quiz(BaseModel):
    """Model representing a quiz."""
    questions: list[QuizQuestion]

class QuizRequest(BaseModel):
    """Model representing a request to generate a quiz."""
    learning_objective: str = Field(..., description="The learning objective for the quiz.", min_length=1)
    n_questions: int = Field(2, description="The number of questions to generate.", ge=1)
