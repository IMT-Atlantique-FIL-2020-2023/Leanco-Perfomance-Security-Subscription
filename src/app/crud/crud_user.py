from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user import User


class CRUDUser(CRUDBase[User, None, None]):
    def get_by_login_password(self, db: Session, *, login: str, password: str) -> Optional[User]:
        return db.query(User).filter(User.login == login and User.password == password).first()


user = CRUDUser(User)
