from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomUserCreateForm


class SingUpPageView(generic.CreateView):
    """Регистрация"""
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
