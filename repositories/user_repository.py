from sqlalchemy.orm import Session
from models.base import User
from models.users import UserCreate 

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_data: UserCreate):
        user_data = user_data.model_dump()
        user = User(**user_data)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_all_users(self):
        return self.db.query(User).all()

    def get_user_by_id(self, user_id: str):
        return self.db.query(User).filter_by(user_id=user_id).first()
