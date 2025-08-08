from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from datetime import datetime

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Custom hook before saving
        serializer.save()
        # You can log here, e.g., print(f"Book created by {self.request.user}")

    def create(self, request, *args, **kwargs):
        # Optional: Custom response format
        response = super().create(request, *args, **kwargs)
        return Response({
            "message": "Book successfully created.",
            "data": response.data
        }, status=status.HTTP_201_CREATED)

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({
            "message": "Book successfully updated.",
            "data": response.data
        }, status=status.HTTP_200_OK)
