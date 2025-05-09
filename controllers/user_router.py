from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.users import UserCreate, UserOut
from db.database import get_db
from usecases.user_usecase import UserUseCase

user_router = APIRouter()

@user_router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    uc = UserUseCase(db)
    return uc.create_user(user)

@user_router.get("/", response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)):
    uc = UserUseCase(db)
    return uc.get_users()

@user_router.get("/email/{email}", response_model=UserOut)
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    uc = UserUseCase(db)
    user = uc.get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
