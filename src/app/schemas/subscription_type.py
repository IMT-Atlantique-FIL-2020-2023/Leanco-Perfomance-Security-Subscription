from typing import Optional

from pydantic import BaseModel


class SubscriptionType(BaseModel):
    id: Optional[int] = None
    type: Optional[str] = None

    class Config:
        orm_mode = True

