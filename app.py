from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from models.users import UserCreate, UserOut
from models.base import User, Base
from mangum import Mangum
from database import SessionLocal

app = FastAPI()

# --- Dependency ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Endpoints ---

@app.get("/")
def hello_world():
    return {'message': 'Hello from FastAPI'}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f'Hello from FastAPI, {name}!'}

@app.post("/users/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(
        first_name=user.first_name, 
        last_name=user.last_name,
        is_admin=user.is_admin,
        password=user.password,
        contact_info=user.contact_info,
        status=user.status,
        email=user.email
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/", response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)):
    try:
        return db.query(User).all()
    except Exception as e:
        return {"status": "error", "error": str(e)}

# --- AWS Lambda handler ---
handler = Mangum(app)
