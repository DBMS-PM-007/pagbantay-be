from sqlalchemy.orm import Session
from models.users import UserCreate
from repositories.user_repository import UserRepository

class UserUseCase:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def create_user(self, user: UserCreate):
        return self.repo.create_user(user)

    def get_users(self):
        return self.repo.get_all_users()

