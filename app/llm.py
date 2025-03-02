"""This module provides functions to interact with a language model (LLM) using the aisuite library.

It includes functions to get the LLM client, compute messages for the LLM, and call the LLM model.
It uses AISuite to allow multiple LLM providers to be used interchangeably.
"""
import aisuite as ai

from app import app_config, schemas


def get_llm_client() -> ai.Client:
    """Get the LLM client.

    Returns:
        ai.Client: The AI client.
    """
    return ai.Client({"openai": {"api_key": app_config.OPENAI_API_KEY}})

def compute_llm_messages(system_prompt: str, user_prompt: str) -> list[dict[str, str]]:
    """Get the LLM messages.

    Args:
        system_prompt (str): The system prompt for the LLM.
        user_prompt (str): The user prompt for the LLM.

    Returns:
        list[dict[str, str]]: The list of messages for the LLM.
    """
    return [
        schemas.LLMMessage(role="system", content=system_prompt).model_dump(),
        schemas.LLMMessage(role="user", content=user_prompt).model_dump(),
    ]

def call_llm(messages: list[dict[str, str]], **kwargs) -> str:
    """Call the LLM model.

    Args:
        messages (list[dict[str, str]]): The messages to send to the model.
        **kwargs: Additional arguments for the model call.

    Returns:
        str: The response from the LLM model.
    """
    client: ai.Client = get_llm_client()
    return client.chat.completions.create(
        model=app_config.LLM_MODEL,
        messages=messages,
        response_format={"type": "json_object"},
        **kwargs,
    ).choices[0].message.content
