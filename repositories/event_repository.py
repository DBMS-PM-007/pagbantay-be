from models.base import Event

class EventRepository:
    def __init__(self, db):
        self.db = db

    def create_event(self, event_data):
        event = Event(
            admin_id=event_data.admin_id,   # <-- ADD THIS
            event_name=event_data.event_name,
            date=event_data.date,
            location=event_data.location,
            description=event_data.description
        )
        self.db.add(event)
        self.db.commit()
        self.db.refresh(event)
        return event

    def get_all_events(self):
        return self.db.query(Event).all()
