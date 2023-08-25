from django.db import models
from django.urls import reverse


class BookModel(models.Model):
    """Модель книги"""
    book = models.CharField('Книга', max_length=100)
    author = models.CharField('Автор', max_length=100)
    price = models.PositiveIntegerField('Цена')

    def __str__(self):
        return self.book

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])