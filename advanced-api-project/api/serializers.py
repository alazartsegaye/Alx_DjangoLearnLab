from rest_framework import serializers
from .models import Book, Author

# BookSerializer
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
        print("Validated Data:", validated_data)
        return Book.objects.create(**validated_data)


# AuthorSerializer
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books'] 
