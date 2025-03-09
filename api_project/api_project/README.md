# Book API

## Overview

The Book API is a RESTful API that allows users to manage a collection of books. It supports standard CRUD operations (Create, Read, Update, Delete) and uses token-based authentication to secure access to the endpoints.

## Features

- List all books
- Retrieve details of a specific book
- Create new books
- Update existing books
- Delete books
- Token-based authentication for secure access

## Authentication

This API uses token-based authentication. To access protected endpoints, you must first obtain an authentication token.

### Obtaining a Token

To obtain a token, send a POST request to the `/api-token-auth/` endpoint with your username and password.

#### Request

```http
POST /api-token-auth/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}

A token for successful authentication:

{
    "token": "your_generated_token"
}

Include the token in the Authorization header for all requests to protected endpoints:

Key: Authorization       Value: Token your_generated_token

