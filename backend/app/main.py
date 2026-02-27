from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .db import SessionLocal
from .models import Car
from .schemas import CarOut
from .auth import login, auth_dep
app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/api/login")
def api_login(data: dict):
    token = login(data["username"], data["password"])
    return {"access_token": token}
@app.get("/api/cars", response_model=list[CarOut], dependencies=[Depends(auth_dep)])
def cars(db: Session = Depends(get_db)):
    return db.query(Car).all()
