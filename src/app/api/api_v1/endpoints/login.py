from datetime import datetime
from typing import Any

import jose.jws
from dateutil.relativedelta import relativedelta
from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.encoders import jsonable_encoder
from jose.constants import ALGORITHMS
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

from app.schemas.user import UserCredentials, User

from app.core.config import settings

router = APIRouter()


# Route pour se connecter et récupérer le type d'abonnement
@router.post("/login", response_model=schemas.LoginResponse)
def login(
    db: Session = Depends(deps.get_db), form_data: UserCredentials = Body(None)
) -> Any:
    # Récupération utilisateur en base
    user = crud.user.get_by_email_password(
        db, email=form_data.email, password=form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=400, detail="Incorrect email or password"
        )

    return {
        "public_ca": settings.SERVER_PUBLIC_CERT,
        "jws": jose.jws.sign(
            jsonable_encoder(
                {
                    # Information de l'utilisateur
                    "user": User.from_orm(user),
                    # Date expiration du jws
                    "exp": int(
                        min(
                            datetime.now() + relativedelta(weeks=+1),
                            datetime.combine(
                                user.subscription_enddate, datetime.min.time()
                            ),
                        ).timestamp()
                    ),
                    # Date de création du jws
                    "iat": int(datetime.today().timestamp()),
                    # Vérification de l'utilisateur
                    "aud": user.email,
                }
            ),
            settings.SERVER_PRIVATE_KEY,
            algorithm=ALGORITHMS.RS384,
        ),
    }
