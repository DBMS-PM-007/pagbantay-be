from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from models.event_availability import EventAvailabilityCreate, EventAvailabilityResponse, EventAvailabilityUpdate
from db.database import get_db
from usecases.event_availability_usecase import EventAvailabilityUseCase

event_availability_router = APIRouter()

@event_availability_router.post("/", response_model=EventAvailabilityResponse)
def create_event_availability(
    availability: EventAvailabilityCreate,
    db: Session = Depends(get_db)
):
    uc = EventAvailabilityUseCase(db)
    return uc.create_event_availability(availability)

@event_availability_router.get("/", response_model=list[EventAvailabilityResponse])
def get_event_availabilities(
    db: Session = Depends(get_db)
):
    uc = EventAvailabilityUseCase(db)
    return uc.get_event_availability()

@event_availability_router.put("/{event_id}", response_model=EventAvailabilityResponse)
def update_event_availability(
    event_id: str, 
    availability: EventAvailabilityUpdate,
    user_id: str = Query(...),
    db: Session = Depends(get_db)
):
    uc = EventAvailabilityUseCase(db)
    return uc.update_event_availability(user_id, event_id, availability)
