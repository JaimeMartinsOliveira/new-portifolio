# tests/test_evolution.py

import pytest
import requests
from unittest.mock import Mock

# Importe a classe que você quer testar
from captcha.evolution import EvolutionAPI


# --- Fixtures de Teste (Dados de setup) ---

# Usa a fixture 'monkeypatch' do pytest para definir variáveis de ambiente temporariamente
@pytest.fixture
def mock_env_vars(monkeypatch):
    """Configura as variáveis de ambiente necessárias para os testes."""
    monkeypatch.setenv("EVOLUTION_API_URL", "http://fake-api.com")
    monkeypatch.setenv("EVOLUTION_API_KEY", "fake-api-key")
    monkeypatch.setenv("EVOLUTION_INSTANCE_NAME", "my-instance")


# --- Testes da Classe EvolutionAPI ---

def test_initialization_success(mock_env_vars):
    """
    Testa se a classe é instanciada corretamente quando as variáveis de ambiente existem.
    """
    api = EvolutionAPI()
    assert api.BASE_URL == "http://fake-api.com"
    assert api.API_KEY == "fake-api-key"
    assert api.INSTANCE_NAME == "my-instance"
    # Acessando o atributo privado para verificação (geralmente não é feito, mas útil em testes)
    assert api._EvolutionAPI__headers['apikey'] == "fake-api-key"


def test_initialization_failure_missing_key(monkeypatch):
    """
    Testa se a classe levanta um ValueError se uma variável de ambiente estiver faltando.
    """
    # Garante que as outras variáveis existem, mas a chave não
    monkeypatch.setenv("EVOLUTION_API_URL", "http://fake-api.com")
    monkeypatch.setenv("EVOLUTION_INSTANCE_NAME", "my-instance")

    with pytest.raises(ValueError, match="As variáveis de ambiente da Evolution API .* não estão configuradas."):
        EvolutionAPI()


def test_send_text_message_success(mock_env_vars, mocker):
    """
    Testa o envio de uma mensagem bem-sucedida, simulando uma resposta 200 OK da API.
    """
    # 1. Mock (simula) a função requests.post
    mock_post = mocker.patch('requests.post')

    # 2. Configura o que o mock deve retornar
    mock_response = Mock()
    mock_response.status_code = 200
    expected_json_response = {'id': '12345', 'status': 'sent'}
    mock_response.json.return_value = expected_json_response
    # O método raise_for_status() não deve fazer nada em caso de sucesso
    mock_response.raise_for_status.return_value = None
    mock_post.return_value = mock_response

    # 3. Executa a função
    api = EvolutionAPI()
    recipient_number = "5548999998888"
    message_text = "Olá, mundo!"
    response = api.send_text_message(number=recipient_number, text=message_text)

    # 4. Verifica os resultados

    # Verifica se a função retornou o JSON esperado
    assert response == expected_json_response

    # Verifica se requests.post foi chamada exatamente uma vez com os argumentos corretos
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
    """
    Testa o comportamento quando a API retorna um erro (ex: 401 Unauthorized).
    """
    # 1. Mock da função requests.post para simular um erro
    mock_post = mocker.patch('requests.post')

    # 2. Configura o mock para simular uma resposta de erro
    mock_response = Mock()
    mock_response.status_code = 401  # Unauthorized
    # O método raise_for_status() deve levantar um HTTPError
    http_error = requests.exceptions.HTTPError("401 Client Error: Unauthorized for url...")
    http_error.response = mock_response  # anexa a resposta ao erro
    mock_response.raise_for_status.side_effect = http_error
    mock_post.return_value = mock_response

    # 3. Executa a função
    api = EvolutionAPI()
    response = api.send_text_message(number="123", text="teste")

    # 4. Verifica os resultados
    # A função deve capturar a exceção e retornar None
    assert response is None
    mock_post.assert_called_once()  # Garante que a chamada foi tentada


def test_send_text_message_network_error(mock_env_vars, mocker):
    """
    Testa o comportamento em caso de erro de rede (ex: timeout).
    """
    # 1. Mock da função requests.post para levantar uma exceção de rede
    mocker.patch(
        'requests.post',
        side_effect=requests.exceptions.Timeout("Connection timed out")
    )

    # 2. Executa a função
    api = EvolutionAPI()
    response = api.send_text_message(number="123", text="teste")

    # 3. Verifica o resultado
    # A função deve capturar a exceção de timeout e retornar None
    assert response is None