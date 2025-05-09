from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from usecases.admin_access_usecase import AdminAccessService
from models.admin_access import AdminAccessCreate, AdminAccessOut
from db.database import get_db

admin_access_router = APIRouter(tags=["Admin Access"])

@admin_access_router.post("/", response_model=AdminAccessOut)
def grant_admin_access(data: AdminAccessCreate, db: Session = Depends(get_db)):
    service = AdminAccessService(db)
    return service.create_admin_access(data)

@admin_access_router.get("/{user_id}", response_model=bool)
def check_if_admin(user_id: str, db: Session = Depends(get_db)):
    service = AdminAccessService(db)
    return service.is_admin(user_id)

@admin_access_router.get("/", response_model=list[AdminAccessOut])
def list_all_admins(db: Session = Depends(get_db)):
    service = AdminAccessService(db)
    return service.list_admins()

