from sqlalchemy.orm import Session
from models.event_availability import EventAvailabilityCreate
from models.base import Availability

class EventAvailabilityRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_event_availability(self, availability_data: EventAvailabilityCreate):
        availability_data = availability_data.model_dump()
        event_availability = Availability(**availability_data)
        self.db.add(event_availability)
        self.db.commit()
        self.db.refresh(event_availability)
        return event_availability

    def get_event_availability(self):
        return self.db.query(Availability).all()

    def update_event_availability(self, user_id: str, event_id: str, availability_data: EventAvailabilityCreate):
        event_availability = self.db.query(Availability).filter_by(user_id=user_id, event_id=event_id).first()

        if not event_availability:
            return None

        event_availability.station_assignment = availability_data.station_assignment
        event_availability.availability = availability_data.availability

        self.db.commit()
        self.db.refresh(event_availability)
        return event_availability

