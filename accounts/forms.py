from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

"""Расширяют базовые формы пользователей"""


class CustomUserCreateForm(UserCreationForm):
    """Своя форма по созданию пользователя"""
    class Meta:
        model = get_user_model()  # обращается к параметру AUTH_USER_MODEL
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):
    """Своя форма по изменению пользователя"""
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)
