from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from rest_framework import generics

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50

# Post ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def get_queryset(self):
        post_pk = self.kwargs.get('post_pk')
        if post_pk:
            return Comment.objects.filter(post=post_pk).order_by('-created_at')
        return Comment.objects.all().order_by('-created_at')
        
# Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['post_pk']).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if created:
         if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target_content_type=ContentType.objects.get_for_model(post),
                target_object_id=post.id
            )
        return Response({"message": "Post liked successfully."}, status=status.HTTP_201_CREATED)
    return Response({"message": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response({"message": "Post unliked successfully."}, status=status.HTTP_200_OK)
    except Like.DoesNotExist:
        return Response({"message": "You haven't liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)
