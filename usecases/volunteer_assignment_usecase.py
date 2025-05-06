from fastapi import HTTPException
from sqlalchemy.orm import Session
from repositories.user_repository import UserRepository
from repositories.event_repository import EventRepository
from repositories.volunteer_assignment_repository import VolunteerAssignmentRepository
from models.volunteer_assignment import AssignVolunteerRequest

class VolunteerAssignmentUseCase:
    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)
        self.event_repo = EventRepository(db)
        self.assignment_repo = VolunteerAssignmentRepository(db)

    def create_volunteer_assignment(self, assignment_data: AssignVolunteerRequest):
        user = self.user_repo.get_user_by_id(assignment_data.user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        event = self.event_repo.get_event_by_id(assignment_data.event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")

        if self.assignment_repo.is_user_already_assigned(assignment_data.user_id, assignment_data.event_id):
            raise HTTPException(status_code=400, detail="User already assigned to this event")

        return self.assignment_repo.create_assignment(assignment_data)

    def get_volunteer_assignments(self):
        return self.assignment_repo.get_all_assignments()

