from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from models.users import UserCreate, UserOut
from models.base import User, Base
from mangum import Mangum
from db.database import SessionLocal

app = FastAPI()

# --- Endpoints ---

@app.get("/")
def hello_world():
    return {'message': 'Hello from FastAPI'}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f'Hello from FastAPI, {name}!'}

# --- AWS Lambda handler ---
handler = Mangum(app)
