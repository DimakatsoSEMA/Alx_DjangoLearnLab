## 📚 Book API - View Overview

This API provides CRUD operations for Book instances.

### Endpoints

| Method | URL                        | Description                  | Auth Required |
|--------|----------------------------|------------------------------|----------------|
| GET    | /api/books/                | List all books               | ❌ No          |
| GET    | /api/books/<id>/           | Retrieve book by ID          | ❌ No          |
| POST   | /api/books/create/         | Create a new book            | ✅ Yes         |
| PUT    | /api/books/<id>/update/    | Update a book                | ✅ Yes         |
| DELETE | /api/books/<id>/delete/    | Delete a book                | ✅ Yes         |

### Custom Behavior

- `BookSerializer` validates that `publication_year` is not in the future.
- Only authenticated users can create, update, or delete books.
- Responses include a `message` and `data` for clarity.
