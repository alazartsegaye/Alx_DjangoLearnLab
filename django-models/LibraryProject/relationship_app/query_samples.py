from relationship_app.models import Book,Library,Librarian

# Query all books by a specific author
def get_books_by_author(author_id):
    books = Book.objects.filter(author_id=author_id)
    return books

# List all books in a library
def def list_books_in_library(library_id):
    library = Library.objects.get(id=library_id)
    books = library.books.all()  # Assuming a ManyToMany relationship
    return books

# Retrieve the librarian for a library
def get_librarian_for_library(library_id):
    library = Library.objects.get(id=library_id)
    librarian = library.librarian  # Accessing the related librarian
    return librarian
