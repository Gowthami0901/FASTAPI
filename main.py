from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI() # app is an instance 

#myapp = FastAPI()

# @app.get('/') #get request(get is an operation) and path('/')
# def index(): # we can give any name in the place of index for function

#def abc():
    #return 'hii'
    #return{'data': {'name': 'Gowthami'}}


# @app.get('/blog') 
# def index(limit):
#     # only get 10 published blogs
#     return{'data':f'{limit} blogs from the database'}


@app.get('/blog') 
def index(limit = 10,published : bool=True):
    # only get 10 published blogs(http://localhost:8000/blog?limit=15&published=true)
    if published:
        return{'data':f'{limit} published blogs from the database'}
    else:
        return{'data':f'{limit} all the blogs from database'}

# @app.get('/blog/1')
# def show():
#     return {'data': 1}

@app.get('/blog/unpublished')
def unpublished():
    return{'data':'all unpublished blogs'}

# To view all this information use localhost:8000/docs and redocs 


@app.get('/blog/{id}')
def show(id:int):
    return {'data': id}



# @app.get('/blog/{id}/comments')

# def comments(id):
#     # fetch comments of blog with id = id
#     return {'data':{'1','2','3'}}



@app.get('/blog/{id}/comments')

def comments(id, limit=10):
    # fetch comments of blog with id = id (http://localhost:8000/blog/10/comments)
    return limit
    return {'data':{'1','2','3'}}



@app.get('/about') # @app decorated is called as path operation decorator
#def abc():
def xyz():
    return{'data':'about page'}



#### -------Request body---------


# @app.post('/blog')
# def create_blog():
#     return{'data':"blog is created"} (localhost:8000/docs)



# class Blog(BaseModel):
#     pass

# @app.post('/blog')
# def create_blog(request: Blog):
#     return{'data':"blog is created"}


class Blog(BaseModel): # blog model
    title: str
    body: str
    published: Optional[bool]

# @app.post('/blog')
# def create_blog(request: Blog):
#     return request
#     return{'data':"Blog is created"}
@app.post('/blog')
def create_blog(blog: Blog):
    return{'data':f"Blog is created with the title as {blog.title}"}



### ------HOW to Debug-----

@app.post('/blog')
def create_blog(blog: Blog):
    return{'data':f"Blog is created with the title as {blog.title}"}

if __name__ == "__main__": 
    uvicorn.run(app,host="127.0.0.1",port=9000) #localhost:9000




