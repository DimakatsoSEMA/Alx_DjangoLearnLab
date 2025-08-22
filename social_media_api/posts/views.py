from rest_framework import viewsets, permissions, filters, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from notifications.utils import create_notification

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only owners to edit/delete.
    """
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()   

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)  
        like, created = Like.objects.get_or_create(user=request.user, post=post)  
        if created:
            Notification.objects.create(  
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )
            return Response({"detail": "Post liked."}, status=status.HTTP_201_CREATED)
        return Response({"detail": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(post=post, user=request.user).first()
        if like:
            like.delete()
            return Response({"detail": "Post unliked."}, status=status.HTTP_200_OK)
        return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)        return Post.objects.filter(author__in=following_users).order_by('-created_at')
