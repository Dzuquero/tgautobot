
from fastapi import FastAPI
from .database import engine, Base
from .routers import login, cars

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Auto Ads Service")

app.include_router(login.router, prefix="/api")
app.include_router(cars.router, prefix="/api")
