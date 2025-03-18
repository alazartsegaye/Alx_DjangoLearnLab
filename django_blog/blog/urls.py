from django.urls import path
from .views import register, profile, CustomLoginView, CustomLogoutView
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),

     # List all posts
    path('post/', PostListView.as_view(), name='post-list'),

    # View a single post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # Create a new post
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    # Update an existing post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    # Delete a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
