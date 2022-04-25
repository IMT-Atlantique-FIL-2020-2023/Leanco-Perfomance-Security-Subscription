from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.app.db.base_class import Base

class SubscriptionType(Base):
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    type = Column(String, nullable=False)
    users = relationship("User", back_populates="subscription_type")
