# Update the title of the book
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
updated_book = Book.objects.get(id=book.id)
updated_book.title  # 'Nineteen Eighty-Four'

# Expected Output:
# updated_book.title => 'Nineteen Eighty-Four'
