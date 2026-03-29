from fastapi import HTTPException, status

from app.core.security import create_access_token, hash_password, verify_password
from app.models.user_model import new_user
from app.repositories.user_repository import UserRepository
from app.schemas.auth_schema import LoginRequest
from app.schemas.user_schema import UserCreate


class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def register(self, payload: UserCreate):
        existing = self.user_repo.get_by_email(payload.email)
        if existing:
            raise HTTPException(status_code=400, detail="Email already registered")

        user = new_user(
            name=payload.name,
            email=payload.email,
            hashed_password=hash_password(payload.password),
            role=payload.role,
        )
        created = self.user_repo.create(user)
        return create_access_token(str(created["_id"]))

    def login(self, payload: LoginRequest):
        user = self.user_repo.get_by_email(payload.email)
        if not user or not verify_password(payload.password, user["password"]):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

        if user["role"] == "doctor" and not user.get("is_approved", False):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Doctor not approved")

        return create_access_token(str(user["_id"]))
