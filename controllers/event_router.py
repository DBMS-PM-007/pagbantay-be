from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from models.event import EventCreate, EventResponse, EventUpdate 
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

@event_router.get("/{event_id}", response_model=EventResponse)
def get_event_by_id(event_id: str, usecase: EventUseCase = Depends(get_event_usecase)):
    return usecase.get_event_by_id(event_id)

@event_router.put("/{event_id}", response_model=EventResponse)
def update_event(event_id: str, event_data: EventUpdate, usecase: EventUseCase = Depends(get_event_usecase)):
    return usecase.update_event(event_id, event_data)