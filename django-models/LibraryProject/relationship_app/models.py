from django.db import models

class Author(models.Model):
    name =  models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.PrimaryField(Author, on_delete=models.CASCADE, related_name='books')

class Library(models.Model):
    name =  models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

class Librarian(models.Model):
    name =  models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
