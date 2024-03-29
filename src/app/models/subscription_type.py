from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..db.base_class import Base


# Modèle SubscriptionType en base
class SubscriptionType(Base):
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    type = Column(String, nullable=False)
    users = relationship("User", back_populates="subscription_type")

    def __str__(self):
        return self.type
