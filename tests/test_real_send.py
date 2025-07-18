import pytest
from dotenv import load_dotenv
import os

# Importe a classe que você quer testar
from captcha.evolution import EvolutionAPI

load_dotenv()


def test_send_real_whatsapp_message():
    recipient_phone = os.getenv('WHATSAPP_RECIPIENT_PHONE')

    assert recipient_phone, "A variável WHATSAPP_RECIPIENT_PHONE não foi encontrada no .env"

    try:
        api = EvolutionAPI()
    except ValueError as e:
        pytest.fail(f"Falha na inicialização da API: {e}. Verifique as variáveis no .env.")

    test_message = "🚀 Mensagem de teste de integração automática! Se você recebeu isso, a API está funcionando."

    print(f"\nEnviando mensagem de teste para: {recipient_phone}")
    print(f"Usando instância: {api.INSTANCE_NAME} na URL: {api.BASE_URL}")

    response = api.send_text_message(number=recipient_phone, text=test_message)

    assert response is not None, "A API não retornou uma resposta. Verifique os logs do contêiner da Evolution API."

    assert 'key' in response or 'id' in response, f"A resposta da API não parece ser de sucesso. Resposta recebida: {response}"

    print(f"✅ Teste de integração bem-sucedido! Resposta da API: {response}")