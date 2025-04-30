from models.event import EventCreate, EventResponse  # Import the Pydantic schemas for input/output validation
from repositories.event_repository import EventRepository  # Import the repository for DB interactions

class EventUseCase:
    def __init__(self, db):
        self.repo = EventRepository(db)  # Initialize repository with DB session

    def create_event(self, event_data: EventCreate) -> EventResponse:
        # Use the repository to create the event in the database
        db_event = self.repo.create_event(event_data)

        # Return a validated response model for the created event
        return EventResponse.model_validate(db_event)

    def get_all_events(self) -> list[EventResponse]:
        # Fetch all events using the repository
        events = self.repo.get_all_events()

        # Return a list of validated EventResponse models for each event
        return [EventResponse.model_validate(event) for event in events]
