
from sqlalchemy import Column, Integer, String
from .database import Base

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, index=True)
    model = Column(String)
    year = Column(Integer)
    price = Column(Integer)
    color = Column(String)
    url = Column(String, unique=True, index=True)
