from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create users
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass123')
        
        # Create sample books
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2022)

    def test_create_book_authenticated(self):
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "author": "Author C",
            "publication_year": 2023
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book_authenticated(self):
        url = reverse('book-update', args=[self.book1.id])
        data = {
            "title": "Book One Updated",
            "author": "Author A",
            "publication_year": 2021
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Book One Updated")

    def test_delete_book_authenticated(self):
        url = reverse('book-delete', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objec
