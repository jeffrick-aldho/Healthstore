from fastapi import APIRouter, Depends

from app.controllers.auth_controller import login_controller, me_controller, register_controller
from app.core.dependencies import get_current_user
from app.schemas.auth_schema import LoginRequest
from app.schemas.user_schema import UserCreate

router = APIRouter()


@router.post("/register")
def register(payload: UserCreate):
    return register_controller(payload)


@router.post("/login")
def login(payload: LoginRequest):
    return login_controller(payload)


@router.get("/me")
def me(user: dict = Depends(get_current_user)):
    return me_controller(user)
