# Retrieve and display all attributes of the book
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title  # "1984"
book.author  # "George Orwell"
book.publication_year  # 1949

# Expected Output:
# book.title => '1984'
# book.author => 'George Orwell'
# book.publication_year => 1949
