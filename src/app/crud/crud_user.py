from hashlib import sha256
from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user import User


# Méthodes CRUD sur la table USER
class CRUDUser(CRUDBase[User, None, None]):

    # Récupère l'utilisateur à partir de l'email et du mot de passe
    def get_by_email_password(self, db: Session, *, email: str, password: str) -> Optional[User]:
        return db.query(User).filter(User.email == email,
                                     User.password == sha256(password.encode('utf-8')).hexdigest()).first()


user = CRUDUser(User)
