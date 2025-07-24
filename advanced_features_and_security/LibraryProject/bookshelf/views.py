from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import ExampleForm 

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    # handle book creation here
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # handle edit logic
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # handle delete logic
    pass



def example_form_view(request):
    form = ExampleForm(request.POST or None)
    if form.is_valid():
        # Handle the form data safely here
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        # ... e.g., save to DB, send email, etc.
    return render(request, 'bookshelf/form_example.html', {'form': form})
