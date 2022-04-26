from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from ..db.base_class import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    subscription_startdate = Column(Date, nullable=False)
    subscription_enddate = Column(Date, nullable=False)
    company_id = Column(Integer, ForeignKey('company.id'))
    company = relationship("Company", back_populates="users")
    subscription_type_id = Column(Integer, ForeignKey('subscriptiontype.id'))
    subscription_type = relationship("SubscriptionType", back_populates="users")