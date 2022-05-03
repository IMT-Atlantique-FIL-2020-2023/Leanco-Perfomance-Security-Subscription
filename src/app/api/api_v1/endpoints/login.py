from datetime import datetime
from typing import Any

import jose.jws
from dateutil.relativedelta import relativedelta
from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.encoders import jsonable_encoder
from jose.constants import ALGORITHMS
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

from app.schemas.user import UserLogin, UserDto

from app.core.config import settings

router = APIRouter()


@router.post("/login", response_model=schemas.LoginResponse)
def login(db: Session = Depends(deps.get_db), form_data: UserLogin = Body(None)) -> Any:
    user = crud.user.get_by_login_password(db, login=form_data.login, password=form_data.password)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    return {
        "public_ca": settings.SERVER_PUBLIC_CERT,
        "jws": jose.jws.sign(jsonable_encoder(
            {
                'user': UserDto.from_orm(user),
                'exp': min(datetime.now() + relativedelta(weeks=+1),
                           datetime.combine(user.subscription_enddate, datetime.min.time())),
                'iat': datetime.now()
            }), settings.SERVER_PRIVATE_KEY,
            algorithm=ALGORITHMS.RS384)
    }
