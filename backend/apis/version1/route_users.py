from typing import List
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from backend.schemas.users import UserCreate, ShowUser
from backend.db.session import get_db
from backend.db.repository.users import create_new_user, list_users

router = APIRouter()


@router.post("/", response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user


@router.get("/all", response_model=List[ShowUser])
def read_jobs(db: Session = Depends(get_db)):
    users = list_users(db=db)

    return users
