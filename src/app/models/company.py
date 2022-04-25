from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from src.app.db.base_class import Base


class Company(Base):
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    users = relationship("User", back_populates="company")