from pydantic import BaseModel
from typing import Optional

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

    class Config:
        from_attributes = True
