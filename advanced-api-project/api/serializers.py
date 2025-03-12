from rest_framework import serializers
from .models import Book, Author
from rest_framework import generics

# BookSerializer: Serializes all fields of the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # Specifies the model to be serialized
        fields = '__all__'  # Includes all fields of the Book model in the serialized output

    def validate_publication_year(self, value):
        """
        Custom validation to ensure the publication_year is not in the future.
        """
        from django.utils import timezone
        current_year = timezone.now().year  # Get the current year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")  # Use serializers.ValidationError
        return value


# AuthorSerializer: Serializes the Author model and includes nested BookSerializer for related books
class AuthorSerializer(serializers.ModelSerializer):
    # Nested BookSerializer to serialize the related books
    # `books` is the related_name specified in the Book model's ForeignKey field
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author  # Specifies the model to be serialized
        fields = ['id', 'name', 'books']  # Specifies the fields to include in the serialized output

# ListView: Retrieve all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()  # Fetch all books
    serializer_class = BookSerializer  # Use the BookSerializer


# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()  # Fetch a specific book
    serializer_class = BookSerializer  # Use the BookSerializer


# CreateView: Add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()  # Fetch all books (used for validation)
    serializer_class = BookSerializer  # Use the BookSerializer


# UpdateView: Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()  # Fetch a specific book
    serializer_class = BookSerializer  # Use the BookSerializer


# DeleteView: Remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()  # Fetch a specific book
    serializer_class = BookSerializer  # Use the BookSerializer
