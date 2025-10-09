from fastapi import APIRouter, Depends, Form
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from application.services.auth_service import AuthenticationService
from application.model import RegisterUserItem, UserTokenItem
from application.utils.token import create_access_token, get_current_user

authentication_router = APIRouter()
authenticationService = AuthenticationService()

@authentication_router.post("/register", status_code=201)
def register_user(data: RegisterUserItem, user: dict = Depends(get_current_user)):
    return authenticationService.register_user(data, user)

@authentication_router.post("/login", response_model=UserTokenItem)
def user_login(username: str = Form(...), password: str = Form(...)):
    user = authenticationService.authenticate_user(username, password)
    access_token = create_access_token({ "sub": user["$id"], "email": user["email_address"], "username": user["username"] })
    return {
        "id": user.get("$id"),
        "access_token": access_token,
        "token_type": "bearer",
        "full_name": user.get("full_name"),
        "email_address": user.get("email_address"),
        "phone_number": user.get("phone_number"),
        "username": user.get("username")
    }
