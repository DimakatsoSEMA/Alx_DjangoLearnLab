from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer, PublicUserSerializer
from .models import CustomUser   

# Register
class RegisterView(generics.GenericAPIView):  
    serializer_class = RegisterSerializer
    queryset = CustomUser.objects.all()       

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = user.auth_token.key
            return Response({'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Login
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    queryset = CustomUser.objects.all()

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Follow user
class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        if request.user.id == user_id:
            return Response({"detail": "You cannot follow yourself."},
                            status=status.HTTP_400_BAD_REQUEST)
        target = get_object_or_404(CustomUser, id=user_id)
        request.user.following.add(target)
        return Response({
            "detail": f"You are now following {target.username}.",
            "you": PublicUserSerializer(request.user).data,
            "target": PublicUserSerializer(target).data
        }, status=status.HTTP_200_OK)


# Unfollow user
class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        if request.user.id == user_id:
            return Response({"detail": "You cannot unfollow yourself."},
                            status=status.HTTP_400_BAD_REQUEST)
        target = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(target)
        return Response({
            "detail": f"You unfollowed {target.username}.",
            "you": PublicUserSerializer(request.user).data,
            "target": PublicUserSerializer(target).data
        }, status=status.HTTP_200_OK)
