from sqlalchemy.orm import Session
from models.base import AdminAccess
from uuid import uuid4

class AdminAccessRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_id: str) -> AdminAccess:
        admin_access = AdminAccess(admin_id=str(uuid4()), user_id=user_id)
        self.db.add(admin_access)
        self.db.commit()
        self.db.refresh(admin_access)
        return admin_access

    def get_by_user_id(self, user_id: str) -> AdminAccess | None:
        return self.db.query(AdminAccess).filter_by(user_id=user_id).first()

    def get_all(self) -> list[AdminAccess]:
        return self.db.query(AdminAccess).all()

