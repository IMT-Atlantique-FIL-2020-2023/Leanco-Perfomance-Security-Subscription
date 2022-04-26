from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    login: Optional[str] = None
    role: Optional[str] = None
    subscription_startdate: Optional[date] = None
    subscription_enddate: Optional[date] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


class UserLogin(BaseModel):
    login: str
    password: str
