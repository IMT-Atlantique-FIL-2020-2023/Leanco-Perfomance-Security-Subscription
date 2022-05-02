
from pydantic import BaseModel

from app.schemas import UserDto


class LoginResponse(BaseModel):
    user: UserDto

