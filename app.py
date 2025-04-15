from fastapi import FastAPI
from controllers.app_controller import api_controller
from sqlalchemy import Column, Integer, String
from mangum import Mangum

app = FastAPI()

# --- Endpoints ---

@app.get("/")
def hello_world():
    return {'message': 'Hello from FastAPI'}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f'Hello from FastAPI, {name}!'}

# --- App router ---
api_controller(app)

# --- AWS Lambda handler ---
handler = Mangum(app)
