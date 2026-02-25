
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.auth import create_token
from app.config import ADMIN_LOGIN, ADMIN_PASSWORD

router = APIRouter()

class LoginIn(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginIn):
    if data.username != ADMIN_LOGIN or data.password != ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": create_token(data.username)}
