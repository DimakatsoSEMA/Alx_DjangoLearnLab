# relationship_app/query_samples.py

from relationship_app.models import Author, Book

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
