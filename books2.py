from fastapi import FastAPI , Body
from pydantic import BaseModel ,Field
from typing import Optional

app = FastAPI()

# Pydantic Model for Book
class Book:
    id : int 
    title : str
    description : str 
    author : str 
    rating: int 
    def __init__(self , id , title ,description ,author  , rating ):
        self.id = id  
        self.title = title 
        self.description = description 
        self.author = author 
        self.rating = rating
        
BOOKS = [
    Book(  1 ,  "this is first books" , 'fantasy books' , 'author one' ,  5), 
    Book( 2 ,  "this is second books" , 'horror books' , 'author two' ,  4), 
    Book(  3 ,  "this is therd books" , 'classic books' , 'author three' ,  1), 
    Book( 4 ,  "this is fourth books" , 'magic books' , 'author four' ,  5), 
    Book( 5 ,  "this is fifth books" , 'comedy books' , 'author five' ,  2), 
    Book( 6 ,  "this is sixth books" , 'drama books' , 'author six' ,  3), 
    
    
]


# Pydantic Model for POST Requests
class Books_request(BaseModel):
    id :Optional[int] = Field(description="ID is not needed on create " , default=None)  #  Optional field, auto-generated   it may int or none / null  type 
    title : str = Field(min_length=3)
    author : str = Field(min_length=1)
    description : str  = Field(min_length=1 , max_length=100)
    rating: int = Field(gt=0 , lt= 6)
    
    # Example Value for swager docs
    # to create a more descripive request within our Swagger documentaion 
    
    model_config = {
        "json_schema_extra":{
            "example": {
                    "title": "A new Book",
                    "description": "A new Description of a Book",
                    "author": "jithin",
                    "rating": 5
            }
          
        }
    }
    
    
    
    
   
# get all books  ===========

@app.get("/books")
async def read_all_books():
    return BOOKS

#get books with id   (query parameter) =====

@app.get("/books/{book_id}")
async def read_book(book_id : int):
    for b in BOOKS:
        if b.id == book_id:
            return b
        
        
# get book with rating  (Path parameter) ======

@app.get("/books/")
async def read_book_by_rating(book_rating : int):
    books_to_return = [book for book in BOOKS if book.rating == book_rating  ]
    return books_to_return


# create new books =====

@app.post("/create_books")
async def create_new_books(book_request : Books_request ):
    # Create a new book object
    new_books = Book(**book_request.model_dump())    # converting the request to Book object
    new_books.id = BOOKS[-1].id + 1 if BOOKS else 1  # Auto-generate ID
    BOOKS.append(new_books)
    
# def find_book_id(book: Book):
#     if len(BOOKS) > 0 :
#         book.id = BOOKS[-1].id + 1 
#     else:
#         book.id = 1 
     
#     return book
     
    
  
    
    
    



