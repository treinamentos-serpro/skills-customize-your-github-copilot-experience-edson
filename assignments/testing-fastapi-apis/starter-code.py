from fastapi import FastAPI, HTTPException, status
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
    return list(books.values())


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    global next_book_id

    created_book = Book(id=next_book_id, **book.model_dump())
    books[next_book_id] = created_book
    next_book_id += 1
    return created_book


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = books.get(book_id)
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book