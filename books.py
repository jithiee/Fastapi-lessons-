from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'title one'  , 'author' : 'Author one'  , 'category' : 'science'},
    {'title': 'title two'  , 'author' : 'Author two'  , 'category' : 'science'},
    {'title': 'title three'  , 'author' : 'Author three'  , 'category' : 'history'},
    {'title': 'title four'  , 'author' : 'Author four'  , 'category' : 'math'},
    {'title': 'title five'  , 'author' : 'Author five'  , 'category' : 'math'},
    {'title': 'title six'  , 'author' : 'Author six'  , 'category' : 'math'},
]


@app.get('/books')
def get_all_books():
    return BOOKS
