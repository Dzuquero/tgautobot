from jose import jwt
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer
from .config import JWT_SECRET, ADMIN_USER, ADMIN_PASSWORD
security = HTTPBearer()
def login(username: str, password: str):
    if username == ADMIN_USER and password == ADMIN_PASSWORD:
        return jwt.encode({"sub": username}, JWT_SECRET, algorithm="HS256")
    raise HTTPException(401)
def auth_dep(token=Depends(security)):
    try:
        jwt.decode(token.credentials, JWT_SECRET, algorithms=["HS256"])
    except Exception:
        raise HTTPException(401)
