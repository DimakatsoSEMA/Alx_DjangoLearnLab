# Authentication System
## Features
- User Registration with email
- Login and Logout using Django's built-in views
- Profile page to view and update email
## Setup
1. Add `'django.contrib.auth'` and `'django.contrib.sessions'` to INSTALLED_APPS.
2. Run `python manage.py migrate`.
3. Include `blog.urls` in your project `urls.py`.
