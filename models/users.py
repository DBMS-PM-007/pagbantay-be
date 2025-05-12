from pydantic import BaseModel
from typing import Optional, List
from models.volunteer_assignment import AssignVolunteerResponse 
from models.event_availability import EventAvailabilityResponse

# Pydantic schemas for validation and serialization

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    is_admin: bool
    contact_info: str
    status: Optional[str] = None
    email: str

class UserOut(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    email: str
    assignments: Optional[List[AssignVolunteerResponse]] = None
    availability: Optional[List[EventAvailabilityResponse]] = None

    class Config:
        from_attributes = True
