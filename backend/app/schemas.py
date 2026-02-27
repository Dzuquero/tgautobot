from pydantic import BaseModel
class CarOut(BaseModel):
    brand: str
    model: str
    year: int
    price: float
    color: str
    url: str
    class Config:
        orm_mode = True
