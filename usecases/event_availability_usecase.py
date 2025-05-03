from models.event_availability import EventAvailabilityCreate, EventAvailabilityResponse
from repositories.event_availability_repository import EventAvailabilityRepository

class EventAvailabilityUseCase:
    def __init__(self, db):
        self.repo = EventAvailabilityRepository(db)

    def create_event_availability(self, availability_data: EventAvailabilityCreate) -> EventAvailabilityResponse:
        db_availability = self.repo.create_event_availability(availability_data)

        return EventAvailabilityResponse.model_validate(db_availability)

    def get_event_availability(self):
        return self.repo.get_event_availability()

