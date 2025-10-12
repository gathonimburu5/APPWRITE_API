from fastapi import APIRouter, Depends, UploadFile, Form
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from application.services.auth_service import AuthenticationService
from application.model import RegisterUserItem, UserTokenItem, UpdateUserItem, ChangePassword
from application.utils.token import create_access_token, get_current_user
from datetime import date

authentication_router = APIRouter()
authenticationService = AuthenticationService()

@authentication_router.post("/register", status_code=201)
def register_user(
    name: str = Form(...),
    email: str = Form(...),
    username: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...),
    phone: str = Form(...),
    dob: date = Form(...),
    profile: UploadFile = None,
    user: dict = Depends(get_current_user),
    ):
    data = RegisterUserItem(
        full_name=name, email_address=email, username=username, password=password, confirm_password=confirm_password, phone_number=phone, dob=dob, profile=None
    )
    return authenticationService.register_user(data, user, profile)

@authentication_router.get("/users")
def get_users(user: dict = Depends(get_current_user)):
    return authenticationService.get_all_registered_users()

@authentication_router.put("/users", status_code=200)
def update_users(name: str = Form(...), email: str = Form(...), phone: str = Form(...), profile: UploadFile = None, user:dict = Depends(get_current_user)):
    form_data = UpdateUserItem(
        full_name=name, email_address=email, phone_number=phone, profile=None
    )
    status = authenticationService.update_registered_user(form_data, user.get("id"), profile)
    return JSONResponse(content={ "message":"successfully updated user records", "data": status }, status_code=200)

@authentication_router.put("/users/change-passord", status_code=200)
def change_password(old: str = Form(...), new:str = Form(...), confirm:str = Form(...), user:dict = Depends(get_current_user)):
    data = ChangePassword(old_password=old, new_password=new, confirm_password=confirm)
    result = authenticationService.change_user_password(data, user.get("id"))
    return JSONResponse(content=result, status_code=200)

@authentication_router.post("/login", response_model=UserTokenItem)
def user_login(username: str = Form(...), password: str = Form(...)):
    user = authenticationService.authenticate_user(username, password)
    if not user:
        return JSONResponse(content={ "message":"username or password not found, please check!" }, status_code=400)
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
