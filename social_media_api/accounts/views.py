from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer
from .serializers import PublicUserSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = user.auth_token.key
            return Response({'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

User = get_user_model()

class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        if request.user.id == user_id:
            return Response({"detail": "You cannot follow yourself."},
                            status=status.HTTP_400_BAD_REQUEST)
        target = get_object_or_404(User, id=user_id)
        request.user.following.add(target)
        return Response({
            "detail": f"You are now following {target.username}.",
            "you": PublicUserSerializer(request.user).data,
            "target": PublicUserSerializer(target).data
        }, status=status.HTTP_200_OK)


class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        if request.user.id == user_id:
            return Response({"detail": "You cannot unfollow yourself."},
                            status=status.HTTP_400_BAD_REQUEST)
        target = get_object_or_404(User, id=user_id)
        request.user.following.remove(target)
        return Response({
            "detail": f"You unfollowed {target.username}.",
            "you": PublicUserSerializer(request.user).data,
            "target": PublicUserSerializer(target).data
        }, status=status.HTTP_200_OK)
