from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr

from app.schemas.company import Company
from app.schemas.subscription_type import SubscriptionType


class User(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None
    company: Optional[Company] = None
    subscription_startdate: Optional[date] = None
    subscription_enddate: Optional[date] = None
    subscription_type: Optional[SubscriptionType] = None

    class Config:
        orm_mode = True


class UserCredentials(BaseModel):
    email: str
    password: str
