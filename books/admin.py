from django.contrib import admin

from .models import BookModel


class BookAdmin(admin.AdminSite):
    """Выводи нужные поля"""
    list_display = ('book', 'author', 'price')


admin.site.register(BookModel)
