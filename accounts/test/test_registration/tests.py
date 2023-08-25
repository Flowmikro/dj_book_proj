from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SingUpPageTestCase(TestCase):
    """Тестируем функциональность регистрации"""
    username = 'user'
    email = 'user@g.com'

    def setUp(self) -> None:
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_sing_up_template(self):
        """Проверяем используется лм верный html и наличие страницы"""
        self.assertTemplateUsed(self.response, 'account/signup.html')

    def test_signup_model(self):
        """Проверяем как работает регистрация с БД"""
        new_user = get_user_model().objects.create_user(
            self.username,
            self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
