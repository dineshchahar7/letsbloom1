from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from schema.schemas import list_serial, individual_serial

from models.booksModel import Book, BookUpdate
from db.db import collection
from bson import ObjectId
book=APIRouter()

# list books
@book.get("/api/books")
async def get_books():
    gatherData=collection.find()
    # print(gatherData)
    data=list_serial(gatherData)
    # print(data)
    return data

#post books
def is_book_uniqueName(book: Book):
    existing_bookName=collection.find_one({"bookName": book.bookName})
    return existing_bookName is None

def is_book_uniqueId(book: Book):
    existing_bookId=collection.find_one({"bookId": book.bookId})
    return existing_bookId is None

@book.post("/api/books")
async def add_book(request: Request, book: Book = Body(...)):
    try:
        if is_book_uniqueId(book): #handleing duplicate entries of book with same id
            if is_book_uniqueName(book): #handleing duplicate entries of book with same name
                result=collection.insert_one(dict(book))
                return{"status": "Book added", "book_id": str(result.inserted_id)}
        else:
            return{"status": "Book already exists"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


#put books
@book.get("/api/books/{id}")
async def get_book(id: str):
    getbook=collection.find_one({"_id": ObjectId(id)})
    book=individual_serial(getbook)
    # print(getbook)
    return book

@book.put("/api/books/{id}")
async def put_books(id, book: Book):
    existing_book=collection.find_one({"_id":ObjectId(id)})
    if existing_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    result=collection.update_one({"_id": ObjectId(id)}, {"$set": dict(book)})

    if result.modified_count==0:
        raise HTTPException(status_code=500, detail="failed to update book")
    
    return {"message": "Book updated successfully"}
