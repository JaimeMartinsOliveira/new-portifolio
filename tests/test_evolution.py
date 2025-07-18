import pytest
import requests
from unittest.mock import Mock

from captcha.evolution import EvolutionAPI



@pytest.fixture
def mock_env_vars(monkeypatch):
    monkeypatch.setenv("EVOLUTION_API_URL", "http://fake-api.com")
    monkeypatch.setenv("EVOLUTION_API_KEY", "fake-api-key")
    monkeypatch.setenv("EVOLUTION_INSTANCE_NAME", "my-instance")


# --- Testes da Classe EvolutionAPI ---

def test_initialization_success(mock_env_vars):
    api = EvolutionAPI()
    assert api.BASE_URL == "http://fake-api.com"
    assert api.API_KEY == "fake-api-key"
    assert api.INSTANCE_NAME == "my-instance"
    assert api._EvolutionAPI__headers['apikey'] == "fake-api-key"


def test_initialization_failure_missing_key(monkeypatch):
    monkeypatch.setenv("EVOLUTION_API_URL", "http://fake-api.com")
    monkeypatch.setenv("EVOLUTION_INSTANCE_NAME", "my-instance")

    with pytest.raises(ValueError, match="As variáveis de ambiente da Evolution API .* não estão configuradas."):
        EvolutionAPI()


def test_send_text_message_success(mock_env_vars, mocker):
    mock_post = mocker.patch('requests.post')

    mock_response = Mock()
    mock_response.status_code = 200
    expected_json_response = {'id': '12345', 'status': 'sent'}
    mock_response.json.return_value = expected_json_response
    mock_response.raise_for_status.return_value = None
    mock_post.return_value = mock_response

    api = EvolutionAPI()
    recipient_number = "5548999998888"
    message_text = "Olá, mundo!"
    response = api.send_text_message(number=recipient_number, text=message_text)


    assert response == expected_json_response

    expected_url = f"http://fake-api.com/message/sendText/my-instance"
    expected_payload = {
        "number": recipient_number,
        "options": {"delay": 1200, "presence": "composing"},
        "textMessage": {"text": message_text}
    }
    mock_post.assert_called_once_with(
        url=expected_url,
        headers={'apikey': 'fake-api-key', 'Content-Type': 'application/json'},
        json=expected_payload,
        timeout=20
    )


def test_send_text_message_api_error(mock_env_vars, mocker):
    mock_post = mocker.patch('requests.post')

    mock_response = Mock()
    mock_response.status_code = 401
    http_error = requests.exceptions.HTTPError("401 Client Error: Unauthorized for url...")
    http_error.response = mock_response
    mock_response.raise_for_status.side_effect = http_error
    mock_post.return_value = mock_response

    api = EvolutionAPI()
    response = api.send_text_message(number="123", text="teste")

    assert response is None
    mock_post.assert_called_once()


def test_send_text_message_network_error(mock_env_vars, mocker):
    mocker.patch(
        'requests.post',
        side_effect=requests.exceptions.Timeout("Connection timed out")
    )

    api = EvolutionAPI()
    response = api.send_text_message(number="123", text="teste")

    assert response is None