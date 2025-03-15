from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book

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
