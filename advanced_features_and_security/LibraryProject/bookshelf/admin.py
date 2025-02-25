from django.contrib import admin
from .models import Book
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register the Book model with Django Admin
admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')

    # Add filter options based on publication year
    list_filter = ('publication_year',)

    # Add search functionality for title and author
    search_fields = ('title', 'author')

# Register the CustomUser model with the CustomUserAdmin class
admin.site.register(CustomUser, CustomUserAdmin)
