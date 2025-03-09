from django.urls import path, include
from .views import BookViewSet

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
