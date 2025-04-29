from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from models.event import EventCreate, EventResponse
from usecases.event_usecase import EventUseCase
from db.database import get_db

# Create the FastAPI router for events
event_router = APIRouter(tags=["Events"])

# Initialize EventUseCase with the DB session
def get_event_usecase(db: Session = Depends(get_db)):
    return EventUseCase(db)

@event_router.post("/", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
def create_event(event: EventCreate, usecase: EventUseCase = Depends(get_event_usecase)):
    # Creates the event using the event use case
    return usecase.create_event(event)

@event_router.get("/", response_model=list[EventResponse])
def get_events(usecase: EventUseCase = Depends(get_event_usecase)):
    # Retrieves all events using the event use case
    return usecase.get_all_events()
    