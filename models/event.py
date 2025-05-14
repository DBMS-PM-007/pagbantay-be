from pydantic import BaseModel
from pydantic import ConfigDict
from typing import Optional
from datetime import datetime, date

class EventCreate(BaseModel):
    admin_id: str
    event_name: str
    description: str
    location: str
    date: date
    start_time: datetime
    end_time: datetime

class EventResponse(BaseModel):
    event_id: str
    admin_id: str
    event_name: str
    description: str
    location: str
    date: date
    start_time: datetime
    end_time: datetime
    
    model_config = ConfigDict(from_attributes=True)
    
class EventUpdate(BaseModel):
    event_name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    date: Optional[date]
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True) 

