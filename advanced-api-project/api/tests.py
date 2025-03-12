from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Book, Author
from django.contrib.auth.models import User

class BookTests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()

        # Create a test author
        self.author = Author.objects.create(name='J.K. Rowling')

        # Create a test book
        self.book = Book.objects.create(
            title='Harry Potter and the Philosopher\'s Stone',
            author=self.author,
            publication_year=1997,
            isbn='9780747532743'
        )

    def test_create_book(self):
        """
        Ensure we can create a new book.
        """
        self.client.force_authenticate(user=self.user)  # Authenticate the user
        url = reverse('book-create')
        data = {
            'title': 'Harry Potter and the Chamber of Secrets',
            'author': self.author.id,
            'publication_year': 1998,
            'isbn': '9780747538493'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).title, 'Harry Potter and the Chamber of Secrets')

    def test_retrieve_book(self):
        """
        Ensure we can retrieve a book.
        """
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        """
        Ensure we can update a book.
        """
        self.client.force_authenticate(user=self.user)  # Authenticate the user
        url = reverse('book-update', args=[self.book.id])
        data = {'title': 'Updated Title'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(id=self.book.id).title, 'Updated Title')

    def test_delete_book(self):
        """
        Ensure we can delete a book.
        """
        self.client.force_authenticate(user=self.user)  # Authenticate the user
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_publication_year(self):
        """
        Ensure we can filter books by publication year.
        """
        url = reverse('book-list')
        response = self.client.get(url, {'publication_year': 1997}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book.title)

    def test_search_books_by_title(self):
        """
        Ensure we can search books by title.
        """
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Harry'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book.title)

    def test_order_books_by_title(self):
        """
        Ensure we can order books by title.
        """
        # Create a second book for ordering
        Book.objects.create(
            title='A New Book',
            author=self.author,
            publication_year=2000,
            isbn='1234567890123'
        )
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'title'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'A New Book')
        self.assertEqual(response.data[1]['title'], self.book.title)

    def test_unauthenticated_user_cannot_create_book(self):
        """
        Ensure unauthenticated users cannot create books.
        """
        url = reverse('book-create')
        data = {
            'title': 'Unauthorized Book',
            'author': self.author.id,
            'publication_year': 2023,
            'isbn': '1234567890123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
