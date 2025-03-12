from django.db import models

class Author(models.Model):
    """
    Model representing an author.
    """
    name = models.CharField(max_length=255)  # A string field to store the author's name, with a maximum length of 255 characters.

class Book(models.Model):
    """
    Model representing a book.
    """
    title = models.CharField(max_length=255)  # A string field to store the title of the book, with a maximum length of 255 characters.
    publication_year = models.IntegerField()  # An integer field to store the year the book was published.
    
    # A foreign key linking to the Author model.
    # This establishes a one-to-many relationship: one author can have multiple books.
    # If the referenced author is deleted, all related books will also be deleted (due to on_delete=models.CASCADE).
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  
