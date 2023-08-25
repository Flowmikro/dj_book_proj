from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from .forms import CustomUserCreateForm
from .views import SingUpPageView


class CustomUserTestCase(TestCase):
    """Тестируем нашего User"""

    def test_create_user(self):
        """Тестируем создание пользователя"""
        User = get_user_model()
        user = User.objects.create(
            username='test',
            email='test@g.com',
            password='test11233'
        )
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'test@g.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_crete_superuser(self):
        """Тестируем создание суперпользователя"""
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='test admin',
            email='superemail@g.com',
            password='test12345'
        )
        self.assertEqual(admin_user.username, 'test admin')
        self.assertEqual(admin_user.email, 'superemail@g.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SingUpPageTestCase(TestCase):
    """Тестируем функциональность регистрации"""

    def setUp(self) -> None:
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_sing_up_template(self):
        """Проверяем используется лм верный html и наличие страницы"""
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')

    def test_sing_up_form(self):
        """Проверяем используется ли CustomUserCreationForm"""
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreateForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_sing_up_view(self):
        """Проверяет, что при обращении к url будет вызвана правильная функция"""
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SingUpPageView.as_view().__name__
        )

