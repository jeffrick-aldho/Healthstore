import hashlib
from datetime import datetime, timedelta, timezone
from typing import Any

import bcrypt
from jose import JWTError, jwt

from app.core.config import settings


def _password_for_bcrypt(password: str) -> str:
    """SHA-256 hex digest so bcrypt never sees >72 raw bytes (bcrypt limit)."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def hash_password(password: str) -> str:
    prepared = _password_for_bcrypt(password).encode("utf-8")
    return bcrypt.hashpw(prepared, bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        prepared = _password_for_bcrypt(plain_password).encode("utf-8")
        if bcrypt.checkpw(prepared, hashed_password.encode("utf-8")):
            return True
        # Backward compatibility: old raw-bcrypt hashes.
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))
    except ValueError:
        return False


def create_access_token(subject: str, expires_minutes: int | None = None) -> str:
    expire_delta = timedelta(minutes=expires_minutes or settings.jwt_expire_minutes)
    expires_at = datetime.now(timezone.utc) + expire_delta
    payload: dict[str, Any] = {"sub": subject, "exp": expires_at}
    return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)


def decode_access_token(token: str) -> dict[str, Any] | None:
    try:
        return jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
    except JWTError:
        return None
