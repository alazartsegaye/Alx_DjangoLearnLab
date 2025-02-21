from django.urls import path
from .views import list_books, LibraryDetailView, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [ 
        path("books/", list_books, name="list_books"),
        path("library/int:pk/", LibraryDetailView.as_view(), name="library_detail"),
        path('register/', views.register, name='register'),
        path('login/', LoginView.as_view, template_name='login'),
        path('logout/', LogoutView.as_view, template_name='logout'),
]
