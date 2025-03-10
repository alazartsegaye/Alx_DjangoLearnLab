from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookList.as_view(), name='book-list'),
    path('books_all/', BookViewSet.as_view({'get': 'list', 'post': 'create'}), name='book_all'),
]
