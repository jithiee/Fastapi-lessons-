from fastapi import FastAPI , Body

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


# get all books  ===========

@app.get("/books")
async def read_all_books():
    return BOOKS


# create new books =====

@app.post("/create_books")
async def create_new_books(create_books = Body()):
    BOOKS.append(create_books)

