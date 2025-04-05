from sqlalchemy import create_engine
import os

DATABASE_URL = os.environ['DATABASE_URL'].replace("postgresql://", "cockroachdb://")
engine = create_engine(DATABASE_URL)
engine.connect()

print("Connected successfully!")
