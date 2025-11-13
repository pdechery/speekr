# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Speekr is an experimental Twitter-like social media application built with Django 5.2.7, Django Rest Framework 3.16.1, Vue.js, and SQLite. Users can create posts, follow other users, repost content, and quote/comment on posts.

## Development Commands

### Setup and Running
```bash
# Activate virtual environment (if not already active)
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (for admin access)
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Access the app at http://127.0.0.1:8000/
# Admin panel at http://127.0.0.1:8000/admin/
```

### Database and Migrations
```bash
# Create new migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Load fixture data (if available)
python manage.py loaddata speekr/fixtures/<fixture_name>.json
```

### Testing
```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test speekr

# Run specific test file
python manage.py test speekr.tests
```

### Static Files
```bash
# Collect static files for production
python manage.py collectstatic
```

## Architecture

### Custom User Model
- **Critical**: This project uses a custom User model (`speekr.User`) specified in settings as `AUTH_USER_MODEL = 'speekr.User'`
- Always reference users via `settings.AUTH_USER_MODEL` in models, not `django.contrib.auth.models.User`
- User model includes a `follows` ManyToManyField for social following (non-symmetrical)
- Usernames are auto-generated in the format `poster_<random_number>` if not provided

### Core Models
Located in `speekr/models.py`:
- **User**: Custom user with `name` (unique, max 14 chars), `follows` relationship, username auto-generation
- **Post**: User-generated content (max 777 chars), ordered by date descending
- **Repost**: Links to original Post with reposter reference
- **Quote**: Similar to Repost but includes additional commentary (max 200 chars)

### View Organization
Views are split into functional modules in `speekr/views/`:
- `Pages.py`: Template-rendered pages (home, profile)
- `Posts.py`: Post creation API endpoints
- `RepostQuote.py`: Repost and quote creation endpoints
- `Follow.py`: Follow/unfollow functionality
- `Users.py`: User list and detail API views

### URL Structure
- Root URLs handled by `speekr_proj/urls.py`
- App URLs in `speekr/urls.py` with two patterns:
  - Template pages: `/` (home), `/profile/<user_id>` (profile)
  - REST API: `/api/*` endpoints for AJAX operations

### Serializers
Located in `speekr/serializers.py`:
- Use `SlugRelatedField` for user references (via `username` or `name`)
- RepostSerializer and QuoteSerializer override `create()` to handle post_id from validated_data

### Frontend
- Vue.js components in `speekr/static/js/`
- Templates in `speekr/templates/` (home.html, profile.html)
- Hybrid architecture: server-rendered pages + REST API for dynamic updates

### Configuration
- Environment variables managed via `python-decouple`
- `SECRET_KEY` must be set in `.env` file (never commit this)
- SQLite database: `db.sqlite3` in project root
- Static files collected to `static/` directory (STATIC_ROOT)

## Key Implementation Notes

1. **Foreign Key References**: Always use `settings.AUTH_USER_MODEL` for user foreign keys, not direct User model imports
2. **Ordering**: Post, Repost, and Quote models use `ordering = ('-date',)` for reverse chronological display
3. **Related Names**: Posts accessible via `user.posts`, reposts via `post.reposts`, quotes via `post.quotes`
4. **Follow Relationship**: `user.follows` (users they follow), `user.following` (their followers) - non-symmetrical ManyToMany
