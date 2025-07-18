# views.py
from django.http import JsonResponse
from django.utils.timezone import now, timedelta
from .models import PageView
from geoip2.database import Reader
from user_agents import parse as user_agent_parser
import os
import logging  # Importe o módulo de logging

logger = logging.getLogger('user_access')

GEOIP_PATH = os.path.join(os.path.dirname(__file__), 'GeoLite2-City.mmdb')

def register_view(request):
    ip = get_client_ip(request)

    user_agent = request.META.get('HTTP_USER_AGENT', '')
    referrer = request.META.get('HTTP_REFERER', '')
    source = parse_source(referrer)

    logger.info(f"Access IP: {ip}, User-Agent: {user_agent}, Referrer: {referrer}, Source: {source}")

    parsed_agent = user_agent_parser(user_agent)
    browser = f"{parsed_agent.browser.family} {parsed_agent.browser.version_string}"
    os_name = f"{parsed_agent.os.family} {parsed_agent.os.version_string}"

    country, city, region = None, None, None
    try:
        with Reader(GEOIP_PATH) as reader:
            geo_data = reader.city(ip)
            country = geo_data.country.name
            city = geo_data.city.name
            region = geo_data.subdivisions.most_specific.name
    except Exception:
        pass

    '''last_24h = now() - timedelta(hours=24)
    if not PageView.objects.filter(ip_address=ip, timestamp__gte=last_24h).exists():
        PageView.objects.create(
            ip_address=ip,
            user_agent=user_agent,
            referrer=referrer,
            source=source,
            country=country,
            city=city,
            region=region,
            operating_system=os_name,
            browser=browser,
        )
    '''
    PageView.objects.create(
        ip_address=ip,
        user_agent=user_agent,
        referrer=referrer,
        source=source,
        country=country,
        city=city,
        region=region,
        operating_system=os_name,
        browser=browser,
    )

    total_views = PageView.objects.count()

    return JsonResponse({'total_views': total_views})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def parse_source(referrer):
    if not referrer:
        return "Direto"
    elif "google.com" in referrer:
        return "Google"
    elif "facebook.com" in referrer:
        return "Facebook"
    elif "twitter.com" in referrer:
        return "Twitter"
    return "Outros"