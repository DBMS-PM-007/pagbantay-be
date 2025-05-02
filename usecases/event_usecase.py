from models.event import EventCreate, EventResponse
from repositories.event_repository import EventRepository

class EventUseCase:
    def __init__(self, db):
        self.repo = EventRepository(db)

    def create_event(self, event_data: EventCreate) -> EventResponse:
        db_event = self.repo.create_event(event_data)

        return EventResponse.model_validate(db_event)

    def get_all_events(self) -> list[EventResponse]:
        events = self.repo.get_all_events()

        return [EventResponse.model_validate(event) for event in events]
