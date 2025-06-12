# captcha/middleware.py

import requests
import os
import threading
from django.utils.timezone import now, timedelta

notified_ips = {}


def send_whatsapp_notification(request):
    global notified_ips

    path = request.path
    if not path == '/' and not path.startswith('/blog'):
        return

    ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')

    last_notification_time = notified_ips.get(ip_address)
    cooldown = now() - timedelta(hours=1)

    if last_notification_time and last_notification_time > cooldown:
        print(f"Cooldown ativo para o IP: {ip_address}. Notificação não enviada.")
        return

    notified_ips[ip_address] = now()

    api_url = os.environ.get("EVOLUTION_API_URL")
    api_key = os.environ.get("EVOLUTION_API_KEY")
    recipient_phone = os.environ.get("WHATSAPP_RECIPIENT_PHONE")

    if not all([api_url, api_key, recipient_phone]):
        print("AVISO: Credenciais da Evolution API não configuradas no .env. Notificação não enviada.")
        return

    user_agent = request.META.get('HTTP_USER_AGENT', 'N/A')
    message = (
        f"🚀 *Nova Visita no Portfólio!*\n\n"
        f"👤 *IP:* {ip_address}\n"
        f"🌐 *Página:* {request.build_absolute_uri()}"
    )

    headers = {"apiKey": api_key, "Content-Type": "application/json"}
    payload = {
        "number": recipient_phone,
        "options": {"delay": 1200},
        "textMessage": {"text": message}
    }

    try:
        response = requests.post(f"{api_url}/message/sendText", json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        print(f"Notificação de visita enviada com sucesso para {recipient_phone}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar notificação do WhatsApp: {e}")


class VisitorNotificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 200:
            thread = threading.Thread(target=send_whatsapp_notification, args=(request,))
            thread.start()

        return response