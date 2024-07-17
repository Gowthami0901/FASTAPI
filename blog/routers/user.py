
from sqlalchemy.orm import Session
from .. import database, models, schemas
from ..hashing import Hash
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models
from ..repository import user


router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)
get_db=database.get_db

@router.post('/',response_model=schemas.ShowUser,tags=['users'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
     new_user = models.User(name=request.name,email=request.email,password=hashing.Hash.bcrypt(request.password))
     db.add(new_user)
     db.commit()
     db.refresh(new_user)
     return new_user


# def create(request: schemas.User,db:Session):
#     new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# def show(id:int,db:Session):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with the id {id} is not available")
#     return user