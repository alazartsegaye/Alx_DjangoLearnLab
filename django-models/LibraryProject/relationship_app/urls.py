from django.urls import path
from .views import list_books, LibraryDetailView, register, user_login, user_logout

urlpatterns = [ 
        path("books/", list_books, name="list_books"),
        path("library/int:pk/", LibraryDetailView.as_view(), name="library_detail"),
        path('register/', views.register, template_name='register'),
        path('login/', LoginView.as_view, template_name='login'),
        path('logout/', LogoutView.as_view, template_name='logout'),
]
