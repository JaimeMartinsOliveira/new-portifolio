from django.test import TestCase, Client
from django.urls import reverse
from .models import PageView


class PageViewTestCase(TestCase):
    def setUp(self):
        # Configurar cliente e rota para testes
        self.client = Client()
        self.register_url = reverse("register_view")
        self.sample_user_agent = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )

    def test_register_view_creates_page_view(self):
        """
        Testa se o endpoint /captcha/register-view/ cria um registro no banco.
        """
        # Simula uma requisição GET para a rota de registro
        response = self.client.get(
            self.register_url,
            HTTP_USER_AGENT=self.sample_user_agent,
            HTTP_REFERER="https://example.com",
        )

        # Verifica se a resposta é positiva
        self.assertEqual(response.status_code, 200)

        # Verifica se o registro foi criado no banco de dados
        pages = PageView.objects.all()
        self.assertEqual(pages.count(), 1)

        # Valida os dados salvos no banco
        page = pages.first()
        self.assertEqual(page.user_agent, self.sample_user_agent)
        self.assertEqual(page.referrer, "https://example.com")
        self.assertRegex(page.ip_address, r"^\d+\.\d+\.\d+\.\d+$")  # Valida um IP

    def test_register_view_without_user_agent(self):
        """
        Testa se o endpoint funciona sem o cabeçalho User-Agent.
        """
        # Faz uma requisição sem especificar o User-Agent
        response = self.client.get(self.register_url)

        # Verifica o status da resposta
        self.assertEqual(response.status_code, 200)

        # Verifica a criação de um registro no banco
        page = PageView.objects.first()
        self.assertIsNotNone(page)
        self.assertEqual(page.user_agent, "")  # O User-Agent deve estar vazio

    def test_register_view_with_forwarded_ip(self):
        """
        Testa se o IP de um cabeçalho HTTP_X_FORWARDED_FOR é salvo corretamente.
        """
        forwarded_ip = "203.0.113.195"
        response = self.client.get(
            self.register_url,
            HTTP_X_FORWARDED_FOR=forwarded_ip,
            HTTP_USER_AGENT=self.sample_user_agent,
        )

        # Verifica o sucesso da resposta
        self.assertEqual(response.status_code, 200)

        # Valida se o IP fornecido foi salvo corretamente
        page = PageView.objects.first()
        self.assertEqual(page.ip_address, forwarded_ip)

    def test_register_view_creates_multiple_entries(self):
        """
        Testa se múltiplas requisições criam múltiplos registros.
        """
        # Faz três requisições consecutivas
        for _ in range(3):
            self.client.get(self.register_url, HTTP_USER_AGENT=self.sample_user_agent)

        # Verifica se foram criados três registros distintos
        pages = PageView.objects.all()
        self.assertEqual(pages.count(), 3)

    def test_register_view_without_referrer(self):
        """
        Testa se a falta do Referrer não causa erros.
        """
        response = self.client.get(self.register_url, HTTP_USER_AGENT=self.sample_user_agent)

        # Verifica a validade da resposta
        self.assertEqual(response.status_code, 200)

        # Verifica se o referrer no banco de dados está vazio
        page = PageView.objects.first()
        self.assertEqual(page.referrer, "")