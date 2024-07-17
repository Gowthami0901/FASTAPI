from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import blog
from ..oauth2 import get_current_user


router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowBlog],tags=['blogs'])
def all(db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(get_current_user)): #,current_user: schemas.User = Depends(oauth2.get_current_user)):
#     blogs=db.query(models.Blog).all()
    return blog.get_all()


@router.post('/', status_code=status.HTTP_201_CREATED,tags=['blogs'])

def create(request:schemas.Blog, db: Session = Depends(get_db)):
      new_blog = models.Blog(title=request.title, body=request.body)
      db.add(new_blog)
      db.commit()
      db.refresh(new_blog)
      return new_blog

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])

def destroy(id, db: Session = Depends(get_db)):
     db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
     db.commit()
     return 'done'

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED,tags=['blogs'])

def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
     blog= db.query(models.Blog).filter(models.Blog.id==id)
    
     if not blog.first():
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                              detail = f"Blog with id {id} not found")
     
     blog.update(request)  # update({'title':'updated title'})
     db.commit()
     return blog

@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog,tags=['blogs'])

def show(id, db: Session = Depends(get_db)):
      blog = db.query(models.Blog).filter(models.Blog.id==id).first()
      if not blog:
        response.status_code = status.HTTP_404_NOT
      return blog

# @router.post('/', status_code=status.HTTP_201_CREATED,)
# def create(request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return blog.create(request, db)

# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def destroy(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return blog.destroy(id,db)


# @router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
# def update(id:int, request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return blog.update(id,request, db)


# @router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
# def show(id:int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return blog.show(id,db)