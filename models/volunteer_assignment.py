from pydantic import BaseModel
from models.event import EventResponse 
from typing import Optional

class AssignVolunteerRequest(BaseModel):
    user_id: str
    event_id: str

class AssignVolunteerResponse(BaseModel):
    assignment_id: str
    user_id: str
    event_id: str
    event: Optional[EventResponse] = None

    class Config:
        from_attributes = True

