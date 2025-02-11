books = Book.objects.all()

# Display each book
for book in books:
    print(book.title, book.author, book.publication_year)
