from django.contrib import admin

from .models import BookModel, ReviewModel


class BookAdmin(admin.AdminSite):
    """Выводи нужные поля"""
    list_display = ('book', 'author', 'price')


admin.site.register(BookModel)
admin.site.register(ReviewModel)
