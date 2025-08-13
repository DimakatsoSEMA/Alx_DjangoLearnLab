from django.contrib import admin
from django.urls import path, include  # <-- Make sure this line exists

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # <-- Add this line
]
