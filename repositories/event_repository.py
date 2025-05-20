from sqlalchemy.orm import Session
from models.base import Event
from models.event import EventCreate
from models.event import EventUpdate

class EventRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_event(self, event_data: EventCreate):
        event_data = event_data.model_dump()
        event = Event(**event_data)
        self.db.add(event)
        self.db.commit()
        self.db.refresh(event)
        return event

    def get_all_events(self):
        return self.db.query(Event).all()

    def get_event_by_id(self, event_id: str) -> Event | None:
        return self.db.query(Event).filter(Event.event_id == event_id).first()

    def update_event(self, event: Event, event_data: EventUpdate) -> Event:
        event_data_dict = event_data.model_dump(exclude_unset=True)

        for field, value in event_data_dict.items():
            if value is not None:
                setattr(event, field, value)

        self.db.commit()
        self.db.refresh(event)

        return event

    def delete_event(self, event: Event):
        self.db.delete(event)
        self.db.commit()
