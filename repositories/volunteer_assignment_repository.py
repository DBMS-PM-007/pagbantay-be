from models.base import VolunteerAssignment

class VolunteerAssignmentRepository:
    def __init__(self, db):
        self.db = db

    def create_assignment(self, assignment_data):
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
        return assignment

    def get_all_assignments(self):
        return self.db.query(VolunteerAssignment).all()

