from typing import Optional

from pydantic import BaseModel


# Schema Company utilisé par l'API
class Company(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

    class Config:
        orm_mode = True
