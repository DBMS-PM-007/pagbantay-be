from sqlalchemy.orm import Session
from models.event_availability import EventAvailabilityCreate
from models.base import Availability

class EventAvailabilityRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_event_availability(self, availability_data: EventAvailabilityCreate):
        availability_data = availability_data.model_dump()
        event_availability = VolunteerAssignment(**availability_data)
        self.db.add(event_availability)
        self.db.commit()
        self.db.refresh(event_availability)
        return event_availability

    def get_event_availability(self):
        return self.db.query(Availability).all()
