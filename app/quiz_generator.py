"""Module for generating quizzes using LLMs."""
from . import llm, schemas

SYSTEM_PROMPT = f"""
    You are a teacher that is trying to create a quiz for students for a given learning objective.
    For example: 'Balance chemical equations using the law of conservation of mass'
    You'll be asked to generate a list of N questions for the quiz in the following JSON format:

    {schemas.Quiz.model_json_schema()}

    The quiz must follow the following rules:
        1. The questions are multiple-choice with 4 answers to choose from.
        2. One, and only one, of the answers has to be the correct answer.
        3. The output has to be properly formatted in a human-readable form.
        4. The questions must be suited to students in higher education and expressed in English.
"""

def compute_quiz_messages(learning_objective: str, n_questions: int) -> list[dict[str, str]]:
    """Compute the quiz messages.

    Args:
        learning_objective (str): The learning objective for the quiz.
        n_questions (int): The number of questions to generate.

    Returns:
        list[dict[str, str]]: The list of messages for the LLM.
    """
    user_prompt = f"Create a Quiz on {learning_objective} with {n_questions} questions."
    return llm.compute_llm_messages(SYSTEM_PROMPT, user_prompt)

def parse_quiz_from_llm_response(response: str) -> schemas.Quiz:
    """Parse the LLM response.

    Args:
        response (str): The response from the LLM model.

    Returns:
        schemas.Quiz: The parsed quiz questions.
    """
    return schemas.Quiz.model_validate_json(response)

def generate_quiz(learning_objective: str, n_questions: int = 2) -> schemas.Quiz:
    """Generate a set of questions.

    Args:
        learning_objective (str): The learning objective for the quiz.
        n_questions (int, optional): The number of questions to generate. Defaults to 2.

    Returns:
        schemas.Quiz: The generated set of quiz questions.
    """
    quiz_messages = compute_quiz_messages(learning_objective, n_questions)
    response_content = llm.call_llm(quiz_messages)
    return parse_quiz_from_llm_response(response_content)
