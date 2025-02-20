from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)  # Get the author by name
    books = Book.objects.filter(author=author)  # Filter books by the author
    return books

# List all books in a library
def list_books_in_library(library_id):
    library = Library.objects.get(id=library_id)  # Get the library by ID
    books = library.books.all()  # Access all books in the library
    return books

# Retrieve the librarian for a library
def get_librarian_for_library(library_id):
    library = Library.objects.get(id=library_id)  # Get the library by ID
    librarian = Librarian.objects.get(library=library)  # Get the librarian for the library
    return librarian
