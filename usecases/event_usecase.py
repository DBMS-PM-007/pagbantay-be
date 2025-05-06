from models.event import EventCreate, EventResponse, EventUpdate
from repositories.event_repository import EventRepository
from fastapi import HTTPException
from sqlalchemy.orm import Session


class EventUseCase:
    def __init__(self, db: Session):
        self.repo = EventRepository(db)

    def create_event(self, event_data: EventCreate):
        db_event = self.repo.create_event(event_data)

        return EventResponse.model_validate(db_event)

    def get_all_events(self):
        events = self.repo.get_all_events()

        return [EventResponse.model_validate(event) for event in events]

    def get_event_by_id(self, event_id: str) -> EventResponse:
        event = self.repo.get_event_by_id(event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        return EventResponse.model_validate(event)

    def update_event(self, event_id: str, event_data: EventUpdate) -> EventResponse:
        event = self.repo.get_event_by_id(event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")

        update_fields = event_data.model_dump(exclude_unset=True)
        for field, value in update_fields.items():
            setattr(event, field, value)

        self.repo.db.commit()
        self.repo.db.refresh(event)

        return EventResponse.model_validate(event)