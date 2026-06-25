from fastapi import FastAPI, status
from pydantic import BaseModel
from fastapi.exceptions import HTTPException


books = [
    {
        "id" : 1,
        "title" : "The Alchemist",
        "author" : "Paulo Coelho",
        "publish_date" : "1998-01-01"
    },
    {
        "id" : 2,
        "title" : "Sapiens",
        "author" : "Yuval Noah Harari",
        "publish_date" : "2011-01-01"
    },
    {
        "id" : 3,
        "title" : "Atomic Habits",
        "author" : "James Clear",
        "publish_date" : "2018-01-01"
    },
    {
        "id" : 4,
        "title" : "Rich Dad Poor Dad",
        "author" : "Robert Kiyosaki",
        "publish_date" : "2000-01-01"
    },
    {
        "id" : 5,
        "title" : "Think and Grow Rich",
        "author" : "Napoleon Hill",
        "publish_date" : "1937-01-01"
    }
]

app = FastAPI()

# get method
@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_books(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Book not Found")

class Book(BaseModel):
    id: int
    title: str 
    author: str
    publish_date: str

# post method
@app.post("/books")
def create_book(book: Book):
    new_book = book.model_dump()
    books.append(new_book)
    return new_book 


class BookUpdate(BaseModel):
    title: str 
    author: str
    publish_date: str

# put method
@app.put("/book/{book_id}")
def update_book(book_id: int, book_update: BookUpdate):
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update.title
            book['author'] = book_update.author
            book['publish_date'] = book_update.publish_date
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Book not Found")

 
# delete method
@app.delete("/book/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Book not Found")