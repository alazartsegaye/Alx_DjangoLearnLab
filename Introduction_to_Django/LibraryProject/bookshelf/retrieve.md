from bookshelf.models import Book

# Update the title
book = Book.objects.get(title="1984")
book.save()

book
# Expected Output: <Book: 1984>
