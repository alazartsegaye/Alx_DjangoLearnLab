from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet) 

urlpatterns = [
    path('', include(router.urls)),
    path('<int:post_pk>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    path('<int:post_pk>/comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='comment-detail'),
    path('feed/', FeedViewSet.as_view, name='feed')
]
