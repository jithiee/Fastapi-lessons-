from fastapi import Body ,  FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'title one'  , 'author' : 'Author one'  , 'category' : 'science'},
    {'title': 'title two'  , 'author' : 'Author one'  , 'category' : 'math'},
    {'title': 'title three'  , 'author' : 'Author three'  , 'category' : 'history'},
    {'title': 'title four'  , 'author' : 'Author four'  , 'category' : 'math'},
    {'title': 'title five'  , 'author' : 'Author five'  , 'category' : 'math'},
    {'title': 'title six'  , 'author' : 'Author six'  , 'category' : 'math'},
]


@app.get("/books")
async def get_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title : str):
    for books in BOOKS:
        if books.get('title').casefold() == book_title.casefold():
            return books
        
        

# query parameter (GET)  =====================

@app.get("/books/")
async def read_category_query_para(category : str):
    books_to_return = [books for books in BOOKS if books.get('category').casefold() ==  category.casefold()  ]
    return books_to_return


@app.get("/books/{books_author}/")
async def read_author_and_category_query(books_author : str  ,category: str ):
    books_to_return = [books for books in BOOKS if books.get("author").casefold() == books_author.casefold()  and 
                       
                      books.get("category").casefold() == category.casefold()   ]
    
    return books_to_return


# POST HTTP Request ====================================
        
@app.post("/books/create_book")  
async def create_book(new_book = Body()):
    return BOOKS.append(new_book)   
        
        
    
# PUT HTTP Request ====================================

@app.put("/books/update_book")
async def update_books(update_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == update_book.get("title").casefold():
            BOOKS[i] = update_book
     
     
# DELETE HTTP Request ====================================       
            
@app.delete("/books/delete_book/{books_title}")
async def delete_book(books_title : str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == books_title.casefold():
            BOOKS.pop(i)
            break
        
        
        
@app.get("/books/byauthor/{books_authors}/")
async def all_books_spic_author(books_authors: str):
    books_to_return = [ books for books in BOOKS  if books.get("author").casefold()  == books_authors.casefold() ]
    return books_to_return
        
   

        
        
        