from rest_framework import serializers
from .models import Book, Author

# BookSerializer: Serializes all fields of the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_year']

    def validate_publication_year(self, value):
        """
        Custom validation to ensure the publication_year is not in the future.
        """
        from django.utils import timezone
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    def create(self, validated_data):
        print("Validated Data:", validated_data)  # Debugging: Print validated data
        return Book.objects.create(**validated_data)


# AuthorSerializer: Serializes the Author model and includes nested BookSerializer for related books
class AuthorSerializer(serializers.ModelSerializer):
    # Nested BookSerializer to serialize the related books
    # `books` is the related_name specified in the Book model's ForeignKey field
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author  # Specifies the model to be serialized
        fields = ['id', 'name', 'books']  # Specifies the fields to include in the serialized output
