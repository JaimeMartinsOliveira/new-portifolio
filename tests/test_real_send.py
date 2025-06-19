# tests/test_real_send.py

import pytest
from dotenv import load_dotenv
import os

# Importe a classe que você quer testar
from captcha.evolution import EvolutionAPI

# Carrega as variáveis de ambiente do seu arquivo .env
load_dotenv()


# @pytest.mark.skip(reason="Este é um teste de integração que envia uma mensagem real. Descomente para rodar.")
def test_send_real_whatsapp_message():
    """
    Tenta enviar uma mensagem de WhatsApp real usando as configurações do .env.

    ATENÇÃO: Este teste depende que a API da Evolution esteja rodando e
    configurada corretamente. Ele ENVIARÁ uma mensagem de verdade.
    """
    # 1. Busca o número do destinatário do ambiente
    recipient_phone = os.getenv('WHATSAPP_RECIPIENT_PHONE')

    # Validação inicial para garantir que as variáveis foram carregadas
    assert recipient_phone, "A variável WHATSAPP_RECIPIENT_PHONE não foi encontrada no .env"

    # 2. Instancia a classe da API (ela carregará as outras variáveis .env)
    try:
        api = EvolutionAPI()
    except ValueError as e:
        pytest.fail(f"Falha na inicialização da API: {e}. Verifique as variáveis no .env.")

    # 3. Monta e envia a mensagem de teste
    test_message = "🚀 Mensagem de teste de integração automática! Se você recebeu isso, a API está funcionando."

    print(f"\nEnviando mensagem de teste para: {recipient_phone}")
    print(f"Usando instância: {api.INSTANCE_NAME} na URL: {api.BASE_URL}")

    response = api.send_text_message(number=recipient_phone, text=test_message)

    # 4. Verifica o resultado
    # A resposta não deve ser nula
    assert response is not None, "A API não retornou uma resposta. Verifique os logs do contêiner da Evolution API."

    # Uma resposta de sucesso geralmente contém uma chave 'key' ou 'id'
    assert 'key' in response or 'id' in response, f"A resposta da API não parece ser de sucesso. Resposta recebida: {response}"

    print(f"✅ Teste de integração bem-sucedido! Resposta da API: {response}")