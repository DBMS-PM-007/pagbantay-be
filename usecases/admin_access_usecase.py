from repositories.admin_access_repository import AdminAccessRepository
from models.admin_access import AdminAccessCreate
from sqlalchemy.orm import Session
from models.admin_access import AdminAccessOut

class AdminAccessService:
    def __init__(self, db: Session):
        self.repo = AdminAccessRepository(db)

    def create_admin_access(self, data: AdminAccessCreate) -> AdminAccessOut:
        admin = self.repo.create(user_id=data.user_id)
        return AdminAccessOut.from_orm(admin)

    def is_admin(self, user_id: str) -> bool:
        return self.repo.get_by_user_id(user_id) is not None

    def list_admins(self) -> list[AdminAccessOut]:
        admins = self.repo.get_all()
        return [AdminAccessOut.from_orm(a) for a in admins]

