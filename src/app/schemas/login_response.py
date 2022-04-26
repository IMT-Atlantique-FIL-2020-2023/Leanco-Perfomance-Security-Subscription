
from pydantic import BaseModel

from app.schemas import User


class LoginResponse(BaseModel):
    user: User

