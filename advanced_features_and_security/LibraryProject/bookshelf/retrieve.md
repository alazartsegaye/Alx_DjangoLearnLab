from bookshelf.models import Book

# Retrieve book by title
book = Book.objects.get(title="1984")

# Display each book with all attributes
for book in books:
    print(book.title, book.author, book.publication_year)
# Expected Output: <1984 George Orwell 1949>
