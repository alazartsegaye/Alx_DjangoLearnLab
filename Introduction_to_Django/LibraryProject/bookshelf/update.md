book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

book
# Expected Output: <Book: Nineteen Eighty-Four>
