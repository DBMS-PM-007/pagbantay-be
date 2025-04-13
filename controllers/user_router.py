from fastapi import APIRouter, Path
from sqlalchemy.orm import Session
from models.users import UserCreate, UserOut
from db.database import get_db
from usecase.user_usecase import UserUseCase

user_router = APIRouter()

@user_router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    uc = UserUseCase(db)
    return uc.create_user(user)

@user_router.post("/" response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)):
    uc = UserUseCase(db)
    return uc.get_users()
