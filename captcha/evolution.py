# captcha/evolution.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()


class EvolutionAPI:
    BASE_URL = os.getenv('EVOLUTION_API_URL')
    API_KEY = os.getenv('EVOLUTION_API_KEY')
    INSTANCE_NAME = os.getenv('EVOLUTION_INSTANCE_NAME')

    def __init__(self):
        if not all([self.BASE_URL, self.API_KEY, self.INSTANCE_NAME]):
            raise ValueError("As variáveis de ambiente da Evolution API (URL, KEY, INSTANCE_NAME) não estão configuradas.")

        self.__headers = {
            'apikey': self.API_KEY,
            'Content-Type': 'application/json'
        }

    def send_text_message(self, number: str, text: str):
        endpoint = f"{self.BASE_URL}/message/sendText/{self.INSTANCE_NAME}"

        payload = {
            "number": number,
            "options": {"delay": 1200, "presence": "composing"},
            "textMessage": {"text": text}
        }

        try:
            response = requests.post(
                url=endpoint,
                headers=self.__headers,
                json=payload,
                timeout=20
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            error_message = f"Erro ao enviar mensagem via Evolution API: {e}"
            if e.response:
                error_message += f" | Status: {e.response.status_code} | Resposta: {e.response.text}"
            print(error_message)
            return None