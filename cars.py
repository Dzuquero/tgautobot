
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Car
from app.schemas import CarOut
from app.auth import verify_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/cars", response_model=list[CarOut])
def get_cars(
    brand: str | None = None,
    color: str | None = None,
    max_price: int | None = None,
    db: Session = Depends(get_db),
    _=Depends(verify_token)
):
    query = db.query(Car)
    if brand:
        query = query.filter(Car.brand.ilike(f"%{brand}%"))
    if color:
        query = query.filter(Car.color.ilike(f"%{color}%"))
    if max_price:
        query = query.filter(Car.price <= max_price)
    return query.all()
