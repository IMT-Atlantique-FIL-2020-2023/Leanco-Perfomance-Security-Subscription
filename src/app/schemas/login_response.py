from pydantic import BaseModel


# Schema de la response renvoyée par l'API
class LoginResponse(BaseModel):
    public_ca: str
    jws: str
