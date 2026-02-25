
from jose import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer
from .config import SECRET_KEY

security = HTTPBearer()

def create_token(username: str):
    payload = {"sub": username, "exp": datetime.utcnow() + timedelta(hours=4)}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_token(credentials=Depends(security)):
    try:
        jwt.decode(credentials.credentials, SECRET_KEY, algorithms=["HS256"])
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
