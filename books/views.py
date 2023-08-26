from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from .models import BookModel


class BookListView(ListView):
    """Выводим все книги"""
    model = BookModel
    context_object_name = 'books'
    template_name = 'books/book_list.html'


class BookDetailView(LoginRequiredMixin, DetailView):
    """Полная информация о книге"""
    model = BookModel
    context_object_name = 'book_detail'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
