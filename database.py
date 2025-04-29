from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.utils import Utils
import os

# Load the DATABASE_URL using the utility function
DATABASE_URL = Utils.get_url("/pagbantay-be/database/url")

print(f"Database URL is: {DATABASE_URL}")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set or is empty!")

# Append SSL settings and adapt protocol for CockroachDB
DATABASE_URL += "&sslrootcert=./root.crt"
DATABASE_URL = DATABASE_URL.replace("postgresql://", "cockroachdb://")

# Initialize SQLAlchemy engine and session factory
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Test the database connection manually
try:
    with engine.connect() as connection:
        print("✅ Successfully connected to CockroachDB!")
except Exception as e:
    print("❌ Failed to connect to CockroachDB:", e)

