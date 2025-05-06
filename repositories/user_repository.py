from sqlalchemy.orm import Session
from models.base import User
from models.users import UserCreate 
from sqlalchemy.orm import joinedload

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
        return (
            self.db.query(User)
            .options(joinedload(User.assignments))
            .all()
        )

    def get_user_by_id(self, user_id: str):
        return (
            self.db.query(User)
            .options(joinedload(User.assignments))
            .filter_by(user_id=user_id)
            .first()
        )
