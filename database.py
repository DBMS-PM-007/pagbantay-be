from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv('DATABASE_URL')

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable is not set!")

DATABASE_URL += "&sslrootcert=./root.crt"
DATABASE_URL = DATABASE_URL.replace("postgresql://", "cockroachdb://")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

print("Successfully Connected!")
