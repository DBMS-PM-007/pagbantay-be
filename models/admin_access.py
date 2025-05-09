from pydantic import BaseModel, Field
from typing import Optional
import uuid

class AdminAccessBase(BaseModel):
    user_id: str

class AdminAccessCreate(AdminAccessBase):
    pass

class AdminAccessOut(AdminAccessBase):
    admin_id: str

    class Config:
        from_attributes = True

