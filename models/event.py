from pydantic import BaseModel
from pydantic import ConfigDict  # <- ADD this line
from datetime import date

# This is for incoming request (when user creates an event)
class EventCreate(BaseModel):
    admin_id: int  # <<< you NEED this!
    event_name: str
    date: date
    location: str
    description: str

# This is for response (when you return event details)
class EventResponse(BaseModel):
    event_id: int
    admin_id: int
    event_name: str
    date: date
    location: str
    description: str


    model_config = ConfigDict(from_attributes=True) 
