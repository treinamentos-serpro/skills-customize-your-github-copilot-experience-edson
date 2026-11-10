from fastapi import FastAPI, Response, status
from pydantic import BaseModel

app = FastAPI(title="Book Library API")


class BookCreate(BaseModel):
    title: str
    author: str


class Book(BookCreate):
    id: int


books = {
    1: Book(id=1, title="The Hobbit", author="J.R.R. Tolkien"),
}
next_book_id = 2


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/books", response_model=list[Book])
def list_books():
    # TODO: Return all books.
    pass


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    # TODO: Assign an ID, save the book, and return it.
    pass


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookCreate):
    # TODO: Update the book or return a 404 response.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # TODO: Delete the book or return a 404 response.
    pass