book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

books = Book.objects.all()
print(books)
