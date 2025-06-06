from models.event import EventCreate, EventResponse, EventUpdate, EventDelete
from repositories.event_repository import EventRepository
from fastapi import HTTPException
from sqlalchemy.orm import Session

class EventUseCase:
    def __init__(self, db: Session):
            self.event_repo = EventRepository(db)

    def create_event(self, event_data: EventCreate):
        db_event = self.event_repo.create_event(event_data)

        return EventResponse.model_validate(db_event)

    def get_all_events(self):
        events = self.event_repo.get_all_events()

        return [EventResponse.model_validate(event) for event in events]

    def get_event_by_id(self, event_id: str) -> EventResponse:
        event = self.event_repo.get_event_by_id(event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        return EventResponse.model_validate(event)

    def update_event(self, event_id: str, event_data: EventUpdate) -> EventResponse:
        event = self.event_repo.get_event_by_id(event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")

        updated_event = self.event_repo.update_event(event, event_data)
        return EventResponse.model_validate(updated_event)

    def delete_event(self, event_id: str) -> EventDelete:
        event = self.event_repo.get_event_by_id(event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")

        self.event_repo.delete_event(event)
        return EventDelete(message="Event deleted successfully")

