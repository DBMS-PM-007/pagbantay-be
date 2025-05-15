from enum import Enum
from pydantic import BaseModel
from pydantic import ConfigDict
from models.event import EventResponse 
from typing import Optional

class AvailabilityEnum(str, Enum):
    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"

class EventAvailabilityCreate(BaseModel):
    event_id: str
    user_id: str
    availability: AvailabilityEnum

class EventAvailabilityResponse(BaseModel):
    availability_id: str
    event_id: str
    user_id: str
    availability: AvailabilityEnum
    event: Optional[EventResponse] = None

    model_config = ConfigDict(from_attributes=True)

class EventAvailabilityUpdate(BaseModel):
    availability: AvailabilityEnum
    
    model_config = ConfigDict(from_attributes=True) 

