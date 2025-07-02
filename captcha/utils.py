# captcha/utils.py
import os
import threading
import logging
from .evolution import EvolutionAPI
from .models import CaptchaLog, PageView
from django.utils import timezone
from datetime import timedelta
from ipware import get_client_ip
from django.contrib.gis.geoip2 import GeoIP2
from urllib.parse import urlparse
import user_agents

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def get_source_from_referrer(referrer):
    if not referrer:
        return "Direto"
    parsed_uri = urlparse(referrer)
    domain = parsed_uri.netloc
    if 'google' in domain: return 'Google'
    if 'linkedin' in domain: return 'LinkedIn'
    if 'github' in domain: return 'GitHub'
    if 'facebook' in domain: return 'Facebook'
    if domain == 't.co': return 'Twitter'
    return domain


def save_detailed_page_view(request):
    try:
        ip, _ = get_client_ip(request)
        if ip:
            ua_string = request.META.get('HTTP_USER_AGENT', '')
            user_agent = user_agents.parse(ua_string)
            referrer = request.META.get('HTTP_REFERER')

            page_view = PageView(
                ip_address=ip,
                user_agent=ua_string,
                referrer=referrer,
                source=get_source_from_referrer(referrer),
                operating_system=user_agent.os.family,
                browser=user_agent.browser.family,
            )

            try:
                g = GeoIP2()
                city_data = g.city(ip)
                page_view.country = city_data.get('country_name')
                page_view.city = city_data.get('city')
                page_view.region = city_data.get('region')
            except Exception:
                pass

            page_view.save()
            print(f"PageView salvo para o IP: {ip}")
    except Exception as e:
        print(f"Erro ao salvar PageView: {e}")


def send_whatsapp_notification(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')

    one_hour_ago = timezone.now() - timedelta(hours=1)
    if CaptchaLog.objects.filter(ip_address=ip_address, timestamp__gte=one_hour_ago).exists():
        logging.info(f"Notificação para o IP {ip_address} já foi enviada na última hora. Pulando.")
        return

    recipient_phone = os.getenv('WHATSAPP_RECIPIENT_PHONE')
    if not recipient_phone:
        logging.error("A variável de ambiente WHATSAPP_RECIPIENT_PHONE não está definida.")
        return

    path_info = request.path_info
    logging.info(f"Tentando enviar notificação para o IP: {ip_address} que acessou {path_info}")

    try:
        message = (
            f"🚨 *Alerta de Visita no Portfólio* 🚨\n\n"
            f"Um novo visitante acessou seu site!\n\n"
            f"*IP:* `{ip_address}`\n"
            f"*Página:* `{path_info}`"
        )

        api = EvolutionAPI()

        response = api.send_text_message(number=recipient_phone, text=message)

        if response:
            CaptchaLog.objects.create(ip_address=ip_address, action='notification_sent')
            logging.info(f"Notificação enviada com sucesso para o IP: {ip_address}")
        else:
            logging.error(f"Falha ao enviar notificação para o IP: {ip_address}. Resposta da API foi nula.")

    except Exception as e:
        logging.error(f"Erro inesperado ao processar notificação para o IP {ip_address}: {e}")


def process_first_visit(request):

    notification_thread = threading.Thread(target=send_whatsapp_notification, args=(request,))
    notification_thread.daemon = True
    notification_thread.start()

    page_view_thread = threading.Thread(target=save_detailed_page_view, args=(request,))
    page_view_thread.daemon = True
    page_view_thread.start()