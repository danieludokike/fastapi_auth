from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    username: str
    email: str
    
    
class UserCreate(UserBase):
    password: str
    
    
class UserInDB(UserBase):
    hashed_password: str
    is_active: bool = True
    is_admin: bool = False