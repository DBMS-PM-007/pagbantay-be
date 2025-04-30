from enum import Enum
from datetime import datetime
from pydantic import BaseModel
from pydantic import ConfigDict

class AvailabilityEnum(str, Enum):
    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"

class EventAvailabilityCreate(BaseModel):
    event_id: int
    user_id: int
    station_assignment: str
    availability: AvailabilityEnum

class EventAvailabilityResponse(BaseModel):
    availability_id: int
    event_id: int
    user_id: int
    station_assignment: str
    availability: AvailabilityEnum

    model_config = ConfigDict(from_attributes=True)

