from fastapi import FastAPI , Body
from pydantic import BaseModel ,Field

app = FastAPI()

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



class Books_request(BaseModel):
    id :int 
    title : str = Field(min_length=5)
    author : str = Field(min_length=1)
    description : str  = Field(min_length=1 , max_length=5)
    rating: int = Field(gt=0 , lt= 6)
   
# get all books  ===========

@app.get("/books")
async def read_all_books():
    return BOOKS


# create new books =====

@app.post("/create_books")
async def create_new_books(book_request = Books_request ):
    new_books = Book(**book_request.model_dump())    # converting the request to Book object
    BOOKS.append(find_book_id(new_books))
    
def find_book_id(book: Book):
    if len(Book) > 0 :
        book.id = BOOKS[-1].id + 1 
    else:
        book.id = 1 
     
    return book
     
    
  
    
    
    



