from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import BookModel, ReviewModel


class BookTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testrew',
            email='test@d.com',
            password='test12345'
        )
        self.book = BookModel.objects.create(book='Harry Potter',
                                             author='JK Rowling', price='500', )
        self.review = ReviewModel.objects.create(
            book=self.book,
            user_name=self.user,
            review='testrevi'
        )

    def test_book_model(self):
        """Проверяем BookModel, совпадают ли значения"""
        self.assertEqual(f'{self.book.book}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '500')

    def test_book_list_view(self):
        """Проверяем BookListView"""
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        """Проверяем BookDetailView"""
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertContains(response, 'testrevi')
        self.assertTemplateUsed(response, 'books/book_detail.html')
