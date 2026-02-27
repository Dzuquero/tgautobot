import time
from sqlalchemy.orm import Session
from .db import SessionLocal
from .models import Car
from .scraper import fetch_cars
from .config import SCRAPER_INTERVAL
def upsert(session: Session, car: dict):
    obj = session.query(Car).filter_by(url=car["url"]).first()
    if obj:
        for k, v in car.items():
            setattr(obj, k, v)
    else:
        session.add(Car(**car))
if __name__ == "__main__":
    while True:
        db = SessionLocal()
        for car in fetch_cars():
            upsert(db, car)
        db.commit()
        db.close()
        time.sleep(SCRAPER_INTERVAL)
