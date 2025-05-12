from pydantic import BaseModel
from datetime import datetime
from models.event import EventResponse 
from typing import Optional

class AssignVolunteerRequest(BaseModel):
    event_id: str
    user_id: str
    station: str
    shift_start_time: datetime
    shift_end_time: datetime
    availability_status: str

class AssignVolunteerResponse(BaseModel):
    assignment_id: str
    event_id: str
    event: Optional[EventResponse] = None
    user_id: str
    station: str
    shift_start_time: datetime
    shift_end_time: datetime
    availability_status: str

    class Config:
        from_attributes = True

