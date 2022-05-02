from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr

from app.schemas.subscription_type import SubscriptionType


class UserDto(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    login: Optional[str] = None
    role: Optional[str] = None
    subscription_startdate: Optional[date] = None
    subscription_enddate: Optional[date] = None
    subscription_type: Optional[SubscriptionType] = None

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    login: str
    password: str
