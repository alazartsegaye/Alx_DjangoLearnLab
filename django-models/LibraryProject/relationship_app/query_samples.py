from relationship_app.models import Author,Book,Library,Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.filter(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# List all books in a library
def def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # Assuming a ManyToMany relationship
    return books

# Retrieve the librarian for a library
def get_librarian_for_library(name):
    library = Library.objects.get(name=librarian_name)
    librarian = library.librarian  # Accessing the related librarian
    return librarian
