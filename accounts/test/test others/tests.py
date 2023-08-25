# from django.test import TestCase
# from django.urls import reverse, resolve
#
# from accounts.forms import CustomUserCreateForm
# from accounts.views import SingUpPageView
#
#
# class SingUpPageTestCase(TestCase):
#     """Тестируем функциональность регистрации"""
#
#     def setUp(self) -> None:
#         url = reverse('signup')
#         self.response = self.client.get(url)
#
#     def test_sing_up_template(self):
#         """Проверяем используется лм верный html и наличие страницы"""
#         self.assertEqual(self.response.status_code, 200)
#         self.assertTemplateUsed(self.response, 'registration/signup.html')
#
#     def test_sing_up_form(self):
#         """Проверяем используется ли CustomUserCreationForm"""
#         form = self.response.context.get('form')
#         self.assertIsInstance(form, CustomUserCreateForm)
#         self.assertContains(self.response, 'csrfmiddlewaretoken')
#
#     def test_sing_up_view(self):
#         """Проверяет, что при обращении к url будет вызвана правильная функция"""
#         view = resolve('/accounts/signup/')
#         self.assertEqual(
#             view.func.__name__,
#             SingUpPageView.as_view().__name__
#         )
#
