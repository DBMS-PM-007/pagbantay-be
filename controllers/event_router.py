from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from models.event import EventCreate, EventResponse
from usecases.event_usecase import EventUseCase
from db.database import get_db

event_router = APIRouter(tags=["Events"])

def get_event_usecase(db: Session = Depends(get_db)):
    return EventUseCase(db)

@event_router.post("/", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
def create_event(event: EventCreate, usecase: EventUseCase = Depends(get_event_usecase)):
    return usecase.create_event(event)

@event_router.get("/", response_model=list[EventResponse])
def get_events(usecase: EventUseCase = Depends(get_event_usecase)):
    return usecase.get_all_events()
    
