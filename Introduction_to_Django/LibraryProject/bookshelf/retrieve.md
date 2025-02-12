from bookshelf.models import Book

# Retrieve all books from the database
books = Book.objects.all()

# Display each book with all attributes
for book in books:
    print(book.title, book.author, book.publication_year)
# Expected Output: <1984 George Orwell 1949>
