# Blog CRUD Features

## URLs:
- /posts/ → List all posts
- /posts/new/ → Create a post (login required)
- /posts/<id>/ → View a post
- /posts/<id>/edit/ → Edit post (author only)
- /posts/<id>/delete/ → Delete post (author only)

## Permissions:
- Create → logged-in users
- Edit/Delete → author only
- List/Detail → public

## How to Test:
1. Login as User A → create a post.
2. Logout → confirm you can still view posts.
3. Login as User B → confirm you cannot edit/delete User A's post.
