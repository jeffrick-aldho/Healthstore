from app.utils.helpers import utc_now


def new_user(name: str, email: str, hashed_password: str, role: str) -> dict:
    return {
        "name": name,
        "email": email.lower(),
        "password": hashed_password,
        "role": role,
        "is_approved": role != "doctor",
        "created_at": utc_now(),
    }
