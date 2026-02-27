from sqlalchemy import Column, Integer, String, Float
from .db import Base
class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True)
    brand = Column(String)
    model = Column(String)
    year = Column(Integer)
    price = Column(Float)
    color = Column(String)
    url = Column(String, unique=True)
