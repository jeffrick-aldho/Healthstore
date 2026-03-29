from app.core.database import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.auth_schema import LoginRequest
from app.schemas.user_schema import UserCreate
from app.services.auth_service import AuthService
from app.utils.helpers import serialize_doc
from app.utils.validators import validate_role


def register_controller(payload: UserCreate):
    validate_role(payload.role)
    token = AuthService(UserRepository(get_db())).register(payload)
    return {"access_token": token, "token_type": "bearer"}


def login_controller(payload: LoginRequest):
    token = AuthService(UserRepository(get_db())).login(payload)
    return {"access_token": token, "token_type": "bearer"}


def me_controller(user: dict):
    return serialize_doc(user)
