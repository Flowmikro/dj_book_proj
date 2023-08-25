from django.contrib import admin

from .models import BookModel, ReviewModel


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    """Отображение полей модели BookModel в админке"""
    list_display = ('book', 'author', 'price')


@admin.register(ReviewModel)
class ReviewModelAdmin(admin.ModelAdmin):
    """Отображение полей модели ReviewModel в админке"""
    list_display = ('book', 'user_name', 'review')