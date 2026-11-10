# 📘 Assignment: Testing FastAPI APIs with pytest

## 🎯 Objective

Write automated tests for a FastAPI application using pytest and FastAPI's `TestClient`. Practice checking successful responses, request validation, and error handling without starting a separate web server.

## 📝 Tasks

### 🛠️ Set Up the Test Client

#### Description

Install the required packages, save the provided starter code as `main.py`, and create a `test_api.py` file. Set up a pytest fixture that creates a test client and resets the in-memory book collection before each test.

#### Requirements

The completed tests must:

- Install `fastapi`, `pytest`, and `httpx`.
- Import the application from `main.py` and create a `TestClient` fixture.
- Reset the book collection to its initial sample data before each test.
- Run with `pytest` without starting Uvicorn.

### 🛠️ Test Successful Responses

#### Description

Write tests for the health-check endpoint and for listing and creating books. Verify both response data and relevant HTTP status codes.

#### Requirements

The completed tests must:

- Check that `GET /health` returns status code `200` and `{"status": "ok"}`.
- Check that `GET /books` returns the initial book with its ID, title, and author.
- Check that `POST /books` with a valid title and author returns status code `201` and the created book with an ID.
- Verify that the newly created book appears in a subsequent `GET /books` response.

### 🛠️ Test Validation and Not-Found Errors

#### Description

Test how the API responds to an invalid request body and to a request for a book ID that does not exist.

#### Requirements

The completed tests must:

- Check that `POST /books` without a required field returns status code `422`.
- Check that `GET /books/{book_id}` for an unknown ID returns status code `404`.
- Run the full test suite with `pytest` and confirm all tests pass.