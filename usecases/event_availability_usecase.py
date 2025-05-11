from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.event_availability import EventAvailabilityCreate, EventAvailabilityResponse, EventAvailabilityUpdate
from repositories.event_availability_repository import EventAvailabilityRepository

class EventAvailabilityUseCase:
    def __init__(self, db: Session):
        self.repo = EventAvailabilityRepository(db)

    def create_event_availability(self, availability_data: EventAvailabilityCreate):
        db_availability = self.repo.create_event_availability(availability_data)
        return EventAvailabilityResponse.model_validate(db_availability)

    def get_event_availability(self):
        return self.repo.get_event_availability()

    def update_event_availability(self, user_id: str, event_id: str, availability_data: EventAvailabilityUpdate):
        db_availability = self.repo.update_event_availability(user_id, event_id, availability_data)

        if not db_availability:
            raise HTTPException(status_code=404, detail="Event availability not found")

        return EventAvailabilityResponse.model_validate(db_availability)
