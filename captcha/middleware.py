# captcha/middleware.py
import os
import threading
from django.utils.timezone import now, timedelta
from .evolution import EvolutionAPI

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
        return

    notified_ips[ip_address] = now()

    recipient_phone = os.environ.get("WHATSAPP_RECIPIENT_PHONE")
    if not recipient_phone:
        print("AVISO: Número de celular do destinatário não configurado no .env.")
        return

    message = (
        f"🚀 *Nova Visita no Portfólio!*\n\n"
        f"👤 *IP:* {ip_address}\n"
        f"🌐 *Página:* {request.build_absolute_uri()}"
    )

    try:
        api = EvolutionAPI()
        response = api.send_text_message(number=recipient_phone, text=message)

        if response:
            print(f"Notificação de visita enviada com sucesso para {recipient_phone}")
    except ValueError as e:
        print(e)


class VisitorNotificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 200:
            thread = threading.Thread(target=send_whatsapp_notification, args=(request,))
            thread.start()
        return response