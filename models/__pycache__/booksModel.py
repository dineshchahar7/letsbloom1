from pydantic import BaseModel, Field

class Book(BaseModel):
    bookId: str
    bookName: str=Field(...)
    authorName: str=Field(...)
    quantity: int

class BookUpdate(BaseModel):
    bookId: str
    bookName: str
    authorName: str
    quantity: int