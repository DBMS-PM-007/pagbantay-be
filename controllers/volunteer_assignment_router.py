from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.volunteer_assignment import AssignVolunteerRequest, AssignVolunteerResponse
from db.database import get_db
from usecases.volunteer_assignment_usecase import VolunteerAssignmentUseCase

volunteer_assignment_router = APIRouter()

@volunteer_assignment_router.post("/", response_model=AssignVolunteerResponse)
def create_volunteer_assignment(request: AssignVolunteerRequest, db: Session = Depends(get_db)):
    uc = VolunteerAssignmentUseCase(db)
    return uc.create_volunteer_assignment(request)

@volunteer_assignment_router.get("/", response_model=list[AssignVolunteerResponse])
def get_volunteer_assignments(db: Session = Depends(get_db)):
    uc = VolunteerAssignmentUseCase(db)
    return uc.get_volunteer_assignments()

