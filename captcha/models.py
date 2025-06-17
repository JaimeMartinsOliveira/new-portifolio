# captcha/models.py
from django.db import models
from django.utils import timezone
from django.utils.timezone import now

class CaptchaLog(models.Model):
    ip_address = models.CharField(max_length=45)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.ip_address} - {self.timestamp} - {self.action}'

# Adicione este novo modelo
class PageView(models.Model):
    ip_address = models.GenericIPAddressField()  # IP do visitante
    user_agent = models.TextField(null=True, blank=True)  # Dados do navegador e dispositivo
    referrer = models.URLField(max_length=2048, null=True, blank=True)  # URL de origem (link de chegada)
    source = models.CharField(max_length=255, null=True, blank=True)  # Nome resumido da fonte
    country = models.CharField(max_length=100, null=True, blank=True)  # País
    city = models.CharField(max_length=100, null=True, blank=True)  # Cidade
    region = models.CharField(max_length=100, null=True, blank=True)  # Região ou estado
    operating_system = models.CharField(max_length=50, null=True, blank=True)  # Sistema operacional
    browser = models.CharField(max_length=50, null=True, blank=True)  # Navegador usado
    timestamp = models.DateTimeField(default=now)  # Data e hora da visita

    def __str__(self):
        source_label = self.source or "Desconhecida"
        return f"IP {self.ip_address} - Fonte: {source_label} - {self.timestamp:%d/%m/%Y %H:%M}"

    class Meta:
        verbose_name = "Visualização de Página"
        verbose_name_plural = "Visualizações de Página"
        ordering = ['-timestamp']