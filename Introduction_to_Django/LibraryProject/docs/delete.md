book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Verify deletion by trying to retrieve all books
books = Book.objects.all()
print(books)
