import pytest
from assertpy import assert_that
from app import llm

@pytest.fixture
def sample_messages():
    return [
        {"role": "system", "content": "System prompt"},
        {"role": "user", "content": "User prompt"}
    ]

def test_get_llm_client():
    client = llm.get_llm_client()
    assert_that(client).is_not_none()

def test_compute_llm_messages():
    system_prompt = "System prompt"
    user_prompt = "User prompt"
    messages = llm.compute_llm_messages(system_prompt, user_prompt)
    assert_that(messages).is_length(2)
    assert_that(messages[0]['role']).is_equal_to("system")
    assert_that(messages[1]['role']).is_equal_to("user")

def test_call_llm(mocker, sample_messages):
    mock_client = mocker.patch('app.llm.get_llm_client')
    mock_response = mocker.Mock()
    mock_response.choices = [mocker.Mock()]
    mock_response.choices[0].message.content = "response content"
    mock_client.return_value.chat.completions.create.return_value = mock_response

    response = llm.call_llm(sample_messages)
    assert_that(response).is_equal_to("response content")
