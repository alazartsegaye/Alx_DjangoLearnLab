# Django Blog Project

## Overview
This is a Django-based blog application that allows users to create, read, update, and delete blog posts. It includes features such as user authentication, post tagging, and search functionality. The project is designed to be easy to set up, use, and extend.

## Features
- **User Authentication**: Register, log in, and log out functionality.
- **Blog Posts**: Create, read, update, and delete blog posts.
- **Tagging**: Add tags to blog posts for better organization.
- **Search**: Search for posts by title, content, or tags.

## Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL

### Other Tools
- **Django Allauth**: For authentication
- **Django Taggit**: For tagging

## Getting Started

### Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.8+
- Pip (Python package manager)
- Virtualenv (optional but recommended)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/django-blog.git
    cd django-blog
    ```

2. **Set up a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install (All requirements)
    ```

4. **Set up the database**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser** (to access the Django admin panel):
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

8. **Access the admin panel** at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Project Structure

django-blog/
├── blog/                  # Blog app
│   ├── migrations/        # Database migrations
│   ├── templates/         # HTML templates
│   ├── admin.py           # Admin configuration
│   ├── apps.py            # App configuration
│   ├── forms.py           # Forms for the blog
│   ├── models.py          # Database models
│   ├── urls.py            # URL routing for the blog
│   ├── views.py           # View logic
├── django_blog/           # Project configuration
│   ├── settings.py        # Project settings
│   ├── urls.py            # Main URL routing
│   ├── wsgi.py            # WSGI configuration
├── manage.py              # Django command-line utility
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
