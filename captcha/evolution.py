# captcha/evolution.py

import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()


class EvolutionAPI:
    # Usei nomes um pouco diferentes nas variáveis de ambiente para clareza
    BASE_URL = os.getenv('EVOLUTION_API_URL')
    API_KEY = os.getenv('EVOLUTION_API_KEY')
    INSTANCE_NAME = os.getenv('EVOLUTION_INSTANCE_NAME')  # Opcional, se você usar

    def __init__(self):
        if not all([self.BASE_URL, self.API_KEY]):
            raise ValueError("As variáveis de ambiente da Evolution API não estão configuradas.")

        self.__headers = {
            'apikey': self.API_KEY,
            'Content-Type': 'application/json'
        }

    def send_text_message(self, number: str, text: str):
        """Envia uma mensagem de texto simples."""
        endpoint = f"{self.BASE_URL}/message/sendText"
        # Se você usa múltiplos nomes de instância, pode adicionar o nome aqui.
        # Ex: endpoint = f"{self.BASE_URL}/message/sendText/{self.INSTANCE_NAME}"

        payload = {
            "number": number,
            "options": {"delay": 1200},
            "textMessage": {"text": text}
        }

        try:
            response = requests.post(
                url=endpoint,
                headers=self.__headers,
                json=payload,
                timeout=10  # Adiciona um timeout para segurança
            )
            response.raise_for_status()  # Lança um erro para respostas 4xx/5xx
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem via Evolution API: {e}")
            return None