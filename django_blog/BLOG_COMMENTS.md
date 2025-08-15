# Comment System

## URLs:
- /posts/<post_id>/comments/new/ → Add a comment (login required)
- /comments/<comment_id>/edit/ → Edit comment (author only)
- /comments/<comment_id>/delete/ → Delete comment (author only)

## Features:
- Authenticated users can comment on posts.
- Only the comment author can edit or delete their comment.
- Comments appear under the related post on the post detail page.

## How to Test:
1. Log in as User A → add comment.
2. Confirm it appears under the post.
3. Log in as another user → confirm you cannot edit/delete other users’ comments.
