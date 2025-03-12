from rest_framework import serializers
from .models import Book, Author

# BookSerializer: Serializes all fields of the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # Specifies the model to be serialized
        fields = '__all__'  # Includes all fields of the Book model in the serialized output

# AuthorSerializer: Serializes the Author model and includes nested BookSerializer for related books
class AuthorSerializer(serializers.ModelSerializer):
    # Nested BookSerializer to serialize the related books
    # `books` is the related_name specified in the Book model's ForeignKey field
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author  # Specifies the model to be serialized
        fields = ['id', 'name', 'books']  # Specifies the fields to include in the serialized output
