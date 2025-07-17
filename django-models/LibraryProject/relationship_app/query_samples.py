# relationship_app/query_samples.py

from relationship_app.models import Author, Book

def run_queries():
    # 1. Query all books by a specific author
    author_name = "J.K. Rowling"
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = author.books.all()
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author named '{author_name}' found.")

    # 2. List all books in a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        print(f"\nBooks in {library_name}:")
        for book in books_in_library:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library named '{library_name}' found.")

    # 3. Retrieve the librarian for a library
    try:
        librarian = library.librarian
        print(f"\nLibrarian for {library_name}: {librarian.name}")
    except Exception:
        print(f"Librarian for {library_name} not found or error occurred.")



def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
    except Author.DoesNotExist:
        return []

    # This is the filter query you wanted:
    books = Book.objects.filter(author=author)
    return books

# Example usage
if __name__ == "__main__":
    author_name = "Dimakatso"
    books = get_books_by_author(author_name)
    print(f"Books by {author_name}:")
    for book in books:
        print(f"- {book.title}")
