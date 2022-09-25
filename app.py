from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return { "message": "Hello world!" }

@app.get("/about")
def about():
    return { "say": "I have nothing to say" }

@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished works"}

@app.get("/blog/{blog_id}")
def blog(blog_id: int):
    return {"data": blog_id}

@app.get("/blog/{blog_id}/comments")
def comments(blog_id: int):
 if (blog_id==1):
     return {"comment": "no bs"}
 else:
     return {"0"}