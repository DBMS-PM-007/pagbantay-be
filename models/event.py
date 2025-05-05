from pydantic import BaseModel
from pydantic import ConfigDict
from datetime import date

class EventCreate(BaseModel):
    admin_id: str
    event_name: str
    date: date
    location: str
    description: str

class EventResponse(BaseModel):
    event_id: str
    admin_id: str
    event_name: str
    date: date
    location: str
    description: str

    model_config = ConfigDict(from_attributes=True) 
