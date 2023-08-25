from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class BookModel(models.Model):
    """Модель книги"""
    book = models.CharField('Книга', max_length=100)
    author = models.CharField('Автор', max_length=100)
    image = models.ImageField(upload_to='image/', blank=True)
    price = models.PositiveIntegerField('Цена')

    def __str__(self):
        return self.book

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])


class ReviewModel(models.Model):
    """Отзывы"""
    book = models.ForeignKey(BookModel, verbose_name='Книга', on_delete=models.CASCADE)
    user_name = models.ForeignKey(get_user_model(), verbose_name='Пользователь', on_delete=models.CASCADE)
    review = models.CharField('Отзыв', max_length=300)

    def __str__(self):
        return f'Отзыв на: {str(self.book)}'
