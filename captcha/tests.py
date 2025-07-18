from django.test import TestCase, Client
from django.urls import reverse
from .models import PageView


class PageViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse("register_view")
        self.sample_user_agent = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )

    def test_register_view_creates_page_view(self):
        response = self.client.get(
            self.register_url,
            HTTP_USER_AGENT=self.sample_user_agent,
            HTTP_REFERER="https://example.com",
        )

        self.assertEqual(response.status_code, 200)

        pages = PageView.objects.all()
        self.assertEqual(pages.count(), 1)

        page = pages.first()
        self.assertEqual(page.user_agent, self.sample_user_agent)
        self.assertEqual(page.referrer, "https://example.com")
        self.assertRegex(page.ip_address, r"^\d+\.\d+\.\d+\.\d+$")
    def test_register_view_without_user_agent(self):
        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 200)

        page = PageView.objects.first()
        self.assertIsNotNone(page)
        self.assertEqual(page.user_agent, "")

    def test_register_view_with_forwarded_ip(self):
        forwarded_ip = "203.0.113.195"
        response = self.client.get(
            self.register_url,
            HTTP_X_FORWARDED_FOR=forwarded_ip,
            HTTP_USER_AGENT=self.sample_user_agent,
        )

        self.assertEqual(response.status_code, 200)

        page = PageView.objects.first()
        self.assertEqual(page.ip_address, forwarded_ip)

    def test_register_view_creates_multiple_entries(self):
        for _ in range(3):
            self.client.get(self.register_url, HTTP_USER_AGENT=self.sample_user_agent)

        pages = PageView.objects.all()
        self.assertEqual(pages.count(), 3)

    def test_register_view_without_referrer(self):
        response = self.client.get(self.register_url, HTTP_USER_AGENT=self.sample_user_agent)

        self.assertEqual(response.status_code, 200)

        page = PageView.objects.first()
        self.assertEqual(page.referrer, "")