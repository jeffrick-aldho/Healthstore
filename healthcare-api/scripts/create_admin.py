from app.core.database import get_db
from app.core.security import hash_password


def run(name: str = "Admin", email: str = "admin@example.com", password: str = "Admin@123"):
    db = get_db()
    db["users"].insert_one(
        {
            "name": name,
            "email": email,
            "password": hash_password(password),
            "role": "admin",
            "is_approved": True,
        }
    )
    print(f"Admin user created: {email}")


if __name__ == "__main__":
    run()
