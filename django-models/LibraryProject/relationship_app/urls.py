from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    # Authentication URLs
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # Book CRUD URLs with literal strings required by the check
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
    path('list_books/', views.list_books, name='list_books'),

    # Library detail view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Role-based views
    path('admin_view/', admin_view, name='admin_view'),
    path('librarian_view/', librarian_view, name='librarian_view'),
    path('member_view/', member_view, name='member_view'),
]
