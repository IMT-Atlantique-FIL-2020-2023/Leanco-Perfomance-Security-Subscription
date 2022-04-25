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


# Properties to receive via API on creation
class UserCreate(UserBase):
    firstname: str
    lastname: str
    email: EmailStr
    login: str
    role: str
    subscription_startdate: date
    subscription_enddate: date
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    firstname: str
    lastname: str
    email: EmailStr
    login: str
    role: str
    subscription_startdate: date
    subscription_enddate: date
    password: str


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
