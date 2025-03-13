# Book Management API

## Overview
This is a Django REST Framework (DRF) API for managing books. It provides endpoints for listing, retrieving, creating, updating, and deleting books. The API supports filtering, searching, and ordering of books by various attributes such as title, author, and publication year.

## Features
- **CRUD Operations**: Create, retrieve, update, and delete books.
- **Filtering**: Filter books by `title`, `author`, and `publication_year`.
- **Searching**: Search books by `title` and `author__name`.
- **Ordering**: Order books by `title` and `publication_year`.
- **Authentication**: Only authenticated users can create, update, or delete books.

---

## Installation

### Prerequisites
- Python 3.8+
- Django 4.0+
- Django REST Framework (DRF)

API Endpoints
### 1. List All Books
## URL: /api/books/

Method: GET

Permissions: Public (no authentication required).

Filters:

- **title: Filter by book title.

- **author: Filter by author ID.

- **publication_year: Filter by publication year.

Search:

- **search: Search by title or author__name.

- **Ordering:

- **ordering: Order by title or publication_year (e.g., ?ordering=title).

Example Request:

- **/api/books/?title=Harry&ordering=-publication_year
Example Response:
json

[
    {
        "id": 1,
        "title": "Along Came a Spider",
        "author": 1,
        "publication_year": 1993
    },
    {
        "id": 2,
        "title": "Pop Goes The Weasel",
        "author": 1,
        "publication_year": 1999
    }
]