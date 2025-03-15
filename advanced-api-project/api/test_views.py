from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class BookTests(APITestCase):
    def test_create_book(self):
        url = reverse('book-list')
        data = {'title': 'Test Book', 'author': 'Test Author', 'published_date': '2023-01-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Test Book')
  
    def test_retrieve_book(self):
        book = Book.objects.create(title='Test Book', author='Test Author', published_date='2023-01-01')
        url = reverse('book-detail', args=[book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')
  
    def test_update_book(self):
        book = Book.objects.create(title='Test Book', author='Test Author', published_date='2023-01-01')
        url = reverse('book-detail', args=[book.id])
        data = {'title': 'Updated Book'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get().title, 'Updated Book')
  
    def test_delete_book(self):
        book = Book.objects.create(title='Test Book', author='Test Author', published_date='2023-01-01')
        url = reverse('book-detail', args=[book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

class PermissionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_authenticated_access(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_access(self):
        self.client.credentials()  # Remove authentication
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
