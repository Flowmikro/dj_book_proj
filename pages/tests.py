from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView


class HomePageSimpleTestCase(SimpleTestCase):
    """Тест домашней страницы"""

    def setUp(self) -> None:
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        """Проверяем есть ли страница"""
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_templates(self):
        """Проверяем используется ли верный html шаблон"""
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_url_resolves(self):
        """Проверяет, что при обращении к url будет вызвана правильная функция"""
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutPageSimpleTestCase(SimpleTestCase):
    """Тест about страницы"""
    def setUp(self) -> None:
        url = reverse('about')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        """Проверяем есть ли страница"""
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_templates(self):
        """Проверяем используется ли верный html шаблон"""
        self.assertTemplateUsed(self.response, 'pages/about.html')

    def test_homepage_url_resolves(self):
        """Проверяет, что при обращении к url будет вызвана правильная функция"""
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )


