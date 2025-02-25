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

# Register the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    book_list = ('title', 'author', 'publication_year')

# Function to assign permissions to groups
def assign_permissions_to_groups():
    content_type = ContentType.objects.get_for_model(Book)

    # Get the permissions
    can_view = Permission.objects.get(codename="can_view", content_type=content_type)
    can_create = Permission.objects.get(codename="can_create", content_type=content_type)
    can_edit = Permission.objects.get(codename="can_edit", content_type=content_type)
    can_delete = Permission.objects.get(codename="can_delete", content_type=content_type)

    # Create or get existing groups
    viewers_group, _ = Group.objects.get_or_create(name="Viewers")
    editors_group, _ = Group.objects.get_or_create(name="Editors")
    admins_group, _ = Group.objects.get_or_create(name="Admins")

    # Assign permissions to groups
    viewers_group.permissions.set([can_view])  # Only view
    editors_group.permissions.set([can_view, can_create, can_edit])  # View, create, edit
    admins_group.permissions.set([can_view, can_create, can_edit, can_delete])  # Full access

    # Save groups
    viewers_group.save()
    editors_group.save()
    admins_group.save()

# Call this function to create the groups and permissions
assign_permissions_to_groups()
