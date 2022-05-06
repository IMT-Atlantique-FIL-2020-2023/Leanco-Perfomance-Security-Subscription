from pydantic import BaseModel


class LoginResponse(BaseModel):
    public_ca: str
    jws: str
