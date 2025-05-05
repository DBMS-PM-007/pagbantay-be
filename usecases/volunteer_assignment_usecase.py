from repositories.volunteer_assignment_repository import VolunteerAssignmentRepository

class VolunteerAssignmentUseCase:
    def __init__(self, db):
        self.repo = VolunteerAssignmentRepository(db)

    def create_volunteer_assignment(self, assignment_data):
        return self.repo.create_assignment(assignment_data)

    def get_volunteer_assignments(self):
        return self.repo.get_all_assignments()

