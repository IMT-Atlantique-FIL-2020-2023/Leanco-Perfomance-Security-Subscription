from hashlib import sha256
from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user import User

from app.core import security


class CRUDUser(CRUDBase[User, None, None]):
    def get_by_login_password(self, db: Session, *, login: str, password: str) -> Optional[User]:
        print(security.get_password_hash(password))
        return db.query(User).filter(User.login == login, User.password == sha256(password.encode('utf-8')).hexdigest()).first()


user = CRUDUser(User)
