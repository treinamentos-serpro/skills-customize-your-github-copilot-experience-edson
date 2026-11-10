# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to practice HTTP methods, request and response models, path operations, and status codes. The API will manage a collection of books stored in memory.

## 📝 Tasks

### 🛠️ Create the API and a Health Check

#### Description

Use the starter code to create a FastAPI application and add a health-check endpoint. Run the application locally and open FastAPI's interactive documentation.

#### Requirements

The completed program must:

- Create a FastAPI application in `main.py`.
- Respond to `GET /health` with `{"status": "ok"}`.
- Run locally with `uvicorn main:app --reload`.
- Make the interactive API documentation available at `/docs`.

### 🛠️ List and Add Books

#### Description

Implement endpoints to retrieve the books in the in-memory collection and add a book using a validated request body.

#### Requirements

The completed program must:

- Respond to `GET /books` with the list of books.
- Accept `POST /books` with a book title and author, assign a unique integer ID, and return the created book with status code `201`.
- Use Pydantic models to validate book data and describe responses.
- Include at least one sample book when the application starts.

Example request body:

```json
{
  "title": "The Little Prince",
  "author": "Antoine de Saint-Exupery"
}
```

### 🛠️ Update and Remove Books

#### Description

Add endpoints to update or remove a book by its ID. Return a clear not-found response when the requested ID does not exist.

#### Requirements

The completed program must:

- Accept `PUT /books/{book_id}` with a title and author and return the updated book.
- Return status code `404` when an update or deletion targets a book that does not exist.
- Accept `DELETE /books/{book_id}` and return status code `204` when a book is removed.
- Keep the collection consistent so removed books no longer appear in `GET /books`.