from django.contrib import admin
from .models import Book, Library
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission

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

class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Library, LibraryAdmin)
admin.site.register(Book)

# Function to assign permissions to groups
def assign_permissions_to_groups():
    # Get the permissions
    can_view_books = Permission.objects.get(codename="can_view_books")
    can_checkout_books = Permission.objects.get(codename="can_checkout_books")
    can_add_books = Permission.objects.get(codename="can_add_books")
    can_remove_books = Permission.objects.get(codename="can_remove_books")

    # Create or get existing groups
    readers_group, created = Group.objects.get_or_create(name="Readers")
    librarians_group, created = Group.objects.get_or_create(name="Librarians")
    admins_group, created = Group.objects.get_or_create(name="Admins")

    # Assign permissions to groups
    readers_group.permissions.add(can_view_books, can_checkout_books)
    librarians_group.permissions.add(can_view_books, can_checkout_books, can_add_books)
    admins_group.permissions.add(can_view_books, can_checkout_books, can_add_books, can_remove_books)

    # Save groups after adding permissions
    readers_group.save()
    librarians_group.save()
    admins_group.save()

# Call this function in a signal, or run manually as needed.
assign_permissions_to_groups()
