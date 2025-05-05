from sqlalchemy.orm import Session
from models.base import VolunteerAssignment
from models.volunteer_assignment import AssignVolunteerRequest

class VolunteerAssignmentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_assignment(self, assignment_data: AssignVolunteerRequest):
        assignment_data = assignment_data.model_dump()
        assignment = VolunteerAssignment(**assignment_data)
        self.db.add(assignment)
        self.db.commit()
        self.db.refresh(assignment)
        return {
            "message": "Volunteer assigned successfully",
            "assignment": assignment,
        }

    def get_all_assignments(self):
        return self.db.query(VolunteerAssignment).all()

    def is_user_already_assigned(self, user_id: str, event_id: str):
        return (
            self.db.query(VolunteerAssignment)
            .filter_by(user_id=user_id, event_id=event_id)
            .first()
            is not None
        )

