from hashlib import sha256
from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user import User


class CRUDUser(CRUDBase[User, None, None]):
    def get_by_email_password(self, db: Session, *, email: str, password: str) -> Optional[User]:
        return db.query(User).filter(User.email == email,
                                     User.password == sha256(password.encode('utf-8')).hexdigest()).first()


user = CRUDUser(User)
