from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
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


class SearchResultsListView(ListView):
    """Поиск книги"""
    model = BookModel
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):
        """Поиск по книге или автору"""
        query = self.request.GET.get('q')
        return BookModel.objects.filter(Q(book__icontains=query | Q(author__icontains=query)))
