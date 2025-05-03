from models.event_availability import EventAvailabilityCreate
from models.base import Availability

class EventAvailabilityRepository:
    def __init__(self, db):
        self.db = db

    def create_event_availability(self, availability_data: EventAvailabilityCreate) -> Availability:
        event_availability = Availability(
            user_id=availability_data.user_id,
            event_id=availability_data.event_id,
            station_assignment=availability_data.station_assignment,
            availability=availability_data.availability
        )
        self.db.add(event_availability)
        self.db.commit()
        self.db.refresh(event_availability)
        return event_availability

    def get_event_availability(self):
        return self.db.query(Availability).all()
