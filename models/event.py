from pydantic import BaseModel
from pydantic import ConfigDict
from typing import Optional
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
    
class EventUpdate(BaseModel):
    event_name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    date: Optional[date] = None

    model_config = ConfigDict(from_attributes=True) 

