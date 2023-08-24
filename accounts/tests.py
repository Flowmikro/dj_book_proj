from django.test import TestCase
from django.contrib.auth import get_user_model


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
