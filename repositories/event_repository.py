from sqlalchemy.orm import Session
from models.base import Event
from models.event import EventCreate

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

    def get_event_by_id(self, event_id: str):
        return self.db.query(Event).filter_by(event_id=event_id).first()
