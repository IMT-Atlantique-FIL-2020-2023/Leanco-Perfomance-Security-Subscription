from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

from app.schemas.user import UserLogin

router = APIRouter()


@router.post("/login", response_model=schemas.LoginResponse)
def login(db: Session = Depends(deps.get_db), form_data: UserLogin = Body(None)) -> Any:
    user = crud.user.get_by_login_password(db, login=form_data.login, password=form_data.password)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    return {
        "user": user,
    }
