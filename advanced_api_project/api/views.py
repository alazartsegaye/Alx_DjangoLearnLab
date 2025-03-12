from rest_framework import generics
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# Book Views
class BookListCreateView(generics.ListCreateAPIView):
    """
    View for listing all books or creating a new book.
    """
    queryset = Book.objects.all()  # Fetch all books
    serializer_class = BookSerializer  # Use the BookSerializer


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, or deleting a specific book.
    """
    queryset = Book.objects.all()  # Fetch a specific book
    serializer_class = BookSerializer  # Use the BookSerializer


# Author Views
class AuthorListCreateView(generics.ListCreateAPIView):
    """
    View for listing all authors or creating a new author.
    """
    queryset = Author.objects.all()  # Fetch all authors
    serializer_class = AuthorSerializer  # Use the AuthorSerializer


class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, or deleting a specific author.
    """
    queryset = Author.objects.all()  # Fetch a specific author
    serializer_class = AuthorSerializer  # Use the AuthorSerializer
