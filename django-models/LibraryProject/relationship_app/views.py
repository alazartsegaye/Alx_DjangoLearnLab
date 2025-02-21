from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [ 
        path("books/", list_books, name="list_books"),
        path("library/int:pk/", LibraryDetailView.as_view(), name="library_detail"),
]

