from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.base import VolunteerAssignment
from repositories.user_repository import UserRepository
from repositories.event_repository import EventRepository

class VolunteerAssignmentRepository:
    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)
        self.event_repo = EventRepository(db)

    def create_assignment(self, assignment_data):
        # Validation
        user = self.user_repo.get_user_by_id(assignment_data.user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        event = self.event_repo.get_event_by_id(assignment_data.event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")

        if self.is_user_already_assigned(assignment_data.user_id, assignment_data.event_id):
            raise HTTPException(status_code=400, detail="User already assigned to this event")

        assignment = VolunteerAssignment(
            event_id=assignment_data.event_id,
            user_id=assignment_data.user_id,
            station=assignment_data.station,
            shift_start_time=assignment_data.shift_start_time,
            shift_end_time=assignment_data.shift_end_time,
            availability_status=assignment_data.availability_status,
        )

        self.db.add(assignment)
        self.db.commit()
        self.db.refresh(assignment)

        return {
            "message": "Volunteer assigned successfully",
            "assignment": assignment,
        }

    def get_all_assignments(self):
        return self.db.query(VolunteerAssignment).all()

    def is_user_already_assigned(self, user_id, event_id):
        return (
            self.db.query(VolunteerAssignment)
            .filter_by(user_id=user_id, event_id=event_id)
            .first()
            is not None
        )

