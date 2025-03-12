from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework
from rest_framework.filters.OrderingFilter import OrderingFilter
from rest_framework.filters.SearchFilter import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# ListView: Retrieve all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()  # Fetch all books
    serializer_class = BookSerializer  # Use the BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]  # Enable filtering and searching
    filterset_fields = ['title', 'author', 'publication_year']  # Fields to filter by
    search_fields = ['title', 'author__name']  # Fields to search on
    ordering_fields = ['title', 'publication_year']  # Fields to order by
    ordering = ['title']  # Default ordering
    permission_classes = [permissions.AllowAny]  # Allow anyone to view the list

# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()  # Fetch a specific book
    serializer_class = BookSerializer  # Use the BookSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to view the list


# CreateView: Add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()  # Fetch all books (used for validation)
    serializer_class = BookSerializer  # Use the BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create books

    def perform_create(self, serializer):
        """
        Custom method to handle additional logic during book creation.
        """
        # Add the current user as the creator of the book (if needed)
        serializer.save(created_by=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Override the create method to customize the response or handle exceptions.
        """
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )



# UpdateView: Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()  # Fetch a specific book
    serializer_class = BookSerializer  # Use the BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can update books

    def perform_update(self, serializer):
        """
        Custom method to handle additional logic during book update.
        """
        # Add custom logic here (e.g., logging the update)
        serializer.save()

    def update(self, request, *args, **kwargs):
        """
        Override the update method to customize the response or handle exceptions.
        """
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )


# DeleteView: Remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()  # Fetch a specific book
    serializer_class = BookSerializer  # Use the BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can delete books
