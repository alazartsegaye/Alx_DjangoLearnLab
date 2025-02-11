from django.contrib import admin
from .models import Book

# Register the Book model with Django Admin
admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')

    # Add filter options based on publication year
    list_filter = ('publication_year',)

    # Add search functionality for title and author
    search_fields = ('title', 'author')
