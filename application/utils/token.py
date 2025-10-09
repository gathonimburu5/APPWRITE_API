import os
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from application.configuration import SECURITY_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi import HTTPException, Depends


oauth_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECURITY_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    try:
        playload = jwt.decode(token, SECURITY_KEY, algorithms=ALGORITHM)
        return playload
    except JWTError:
        return HTTPException(status_code=401, detail="Token expired or it's invalid")

def get_current_user(token: str = Depends(oauth_scheme)):
    payload = decode_access_token(token)
    user_id = payload.get("sub")
    return { "id": user_id, "email": payload.get("email_address"), "username": payload.get("username") }