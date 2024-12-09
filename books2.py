from fastapi import FastAPI , Body , Path , Query , HTTPException
from pydantic import BaseModel ,Field
from typing import Optional
from starlette import status

app = FastAPI()

# Pydantic Model for Book
class Book:
    id : int 
    title : str
    description : str 
    author : str 
    rating: int 
    published_date: int
    def __init__(self , id , title ,description ,author  , rating , publish_date ):
        self.id = id  
        self.title = title 
        self.description = description 
        self.author = author 
        self.rating = rating
        self.published_date = publish_date
        
BOOKS = [
    Book(  1 ,  "this is first books" , 'fantasy books' , 'author one' ,  5 , 2012), 
    Book( 2 ,  "this is second books" , 'horror books' , 'author two' ,  4  , 2012), 
    Book(  3 ,  "this is therd books" , 'classic books' , 'author three' ,  1, 2015), 
    Book( 4 ,  "this is fourth books" , 'magic books' , 'author four' ,  5 , 2014), 
    Book( 5 ,  "this is fifth books" , 'comedy books' , 'author five' ,  2 , 2010), 
    Book( 6 ,  "this is sixth books" , 'drama books' , 'author six' ,  3 , 2016), 
    
    
]


# Pydantic (validation) Model for POST Requests 

class Books_request(BaseModel):
    id :Optional[int] = Field(description="ID is not needed on create " , default=None)  #  Optional field, auto-generated   it may int or none / null  type 
    title : str = Field(min_length=3)
    author : str = Field(min_length=1)
    description : str  = Field(min_length=1 , max_length=100)
    rating: int = Field(gt=0 , lt= 6)
    published_date : int = Field(gt=1999 , lt=2050)
    
    # Example Value for swager docs
    # to create a more descripive request within our Swagger documentaion 

     
    class Config:
           schema_extra = {
                "example": {
                        "title": "A new Book",
                        "description": "A new Description of a Book",
                        "author": "jithin",
                        "rating": 5 ,
                        "publish_date": 2029
                }
            
            }
     
    
    
    
   
# get all books  ===========

@app.get("/books" , status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

#get books with id   ( Path parameter) =====

@app.get("/books/{book_id}" , status_code=status.HTTP_200_OK)
async def read_book(book_id : int = Path(gt=0 , description="Input should be greater than 0")):
    for b in BOOKS:
        if b.id == book_id:
            return b
    raise HTTPException(status_code=404 , detail="item not found")
        
        
# get book with rating  (query parameter) ======

@app.get("/books/" , status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating : int  = Query(gt=0 , lt=6)):
    books_to_return = [book for book in BOOKS if book.rating == book_rating  ]
    return books_to_return


# create new books =====

@app.post("/create_books" , status_code=status.HTTP_201_CREATED) 
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
     
     
# update books ==================



@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_books(book : Books_request):
    book_chnage = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
             BOOKS[i] = book
             book_chnage = True
    if not book_chnage :
        raise HTTPException (status_code= 404 , detail= "item not found")
             
             
             
    
# delete books =======================

@app.delete("/books/{book_id}" , status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id : int = Path(gt= 0)):
    book_change = False 
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id :
            BOOKS.pop(i)
            book_change = True
            break 
    if not book_change :
         raise HTTPException(status_code=404 , detail="item not found")
  
    
@app.get("/books/publish_date/{publish}" , status_code=status.HTTP_200_OK)
async def read_book_by_publish_date(publish_date : int ):
    books_to_return = [ books  for books in BOOKS if books.published_date == publish_date  ]
    if not books_to_return:
        raise HTTPException(status_code=404 , detail= 'itme not found' )
    return books_to_return
    
    



