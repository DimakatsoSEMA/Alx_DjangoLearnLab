# Admin Interface Setup for Book Model

- Registered the `Book` model in `bookshelf/admin.py` using the `@admin.register` decorator.
- Customized admin list view with:
  - Columns: `title`, `author`, `publication_year`
  - Filter sidebar for `publication_year`
  - Search fields for `title` and `author`

## Code snippet:

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')
