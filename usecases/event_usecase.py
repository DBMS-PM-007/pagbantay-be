from models.event import EventCreate, EventResponse
from repositories.event_repository import EventRepository
from fastapi import HTTPException

class EventUseCase:
    def __init__(self, db):
        self.repo = EventRepository(db)

    def create_event(self, event_data: EventCreate) -> EventResponse:
        db_event = self.repo.create_event(event_data)

        return EventResponse.model_validate(db_event)

    def get_all_events(self) -> list[EventResponse]:
        events = self.repo.get_all_events()

        return [EventResponse.model_validate(event) for event in events]

    def get_event_by_id(self, event_id: str) -> EventResponse:
        event = self.repo.get_event_by_id(event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        return EventResponse.model_validate(event)