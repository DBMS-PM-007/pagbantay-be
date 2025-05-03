from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.utils import Utils

DATABASE_URL = Utils.get_url("/pagbantay-be/database/url")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable is not set!")

DATABASE_URL += "&sslrootcert=./root.crt"
DATABASE_URL = DATABASE_URL.replace("postgresql://", "cockroachdb://")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

