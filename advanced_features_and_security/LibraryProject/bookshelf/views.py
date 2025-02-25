from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Library, Book

# View to list books in the library (requires 'can_view_books' permission)
@permission_required('app_name.can_view_books', raise_exception=True)
def library_books(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    books = library.books.all()
    return render(request, 'library_books.html', {'library': library, 'books': books})

# View to checkout a book (requires 'can_checkout_books' permission)
@permission_required('app_name.can_checkout_books', raise_exception=True)
def checkout_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Simulate checking out the book
    # (For simplicity, let's assume checking out simply marks the book as unavailable)
    book.checked_out = True
    book.save()
    return redirect('library_books', library_id=book.library.id)

# View to add a new book to the library (requires 'can_add_books' permission)
@permission_required('app_name.can_add_books', raise_exception=True)
def add_book_to_library(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        description = request.POST['description']
        new_book = Book.objects.create(title=title, author=author, description=description)
        library.books.add(new_book)
        return redirect('library_books', library_id=library.id)
    return render(request, 'add_book.html', {'library': library})

# View to remove a book from the library (requires 'can_remove_books' permission)
@permission_required('app_name.can_remove_books', raise_exception=True)
def remove_book_from_library(request, library_id, book_id):
    library = get_object_or_404(Library, id=library_id)
    book = get_object_or_404(Book, id=book_id)
    library.books.remove(book)
    return redirect('library_books', library_id=library.id)
