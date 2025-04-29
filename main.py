import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from controllers.app_controller import api_controller
from sqlalchemy import create_engine
from db.database import DATABASE_URL


# Initialize FastAPI app
app = FastAPI()

# Check database connection on startup
@app.on_event("startup")
async def startup():
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connection:
            print("✅ Successfully connected to CockroachDB!")
    except Exception as e:
        print(f"❌ Error connecting to CockroachDB: {e}")

# Define a simple root endpoint to handle GET requests to '/'
@app.get("/")
def read_root():
    return {"message": "Welcome to the Pagbantay API!"}

# Register other routes via the controller
api_controller(app)
