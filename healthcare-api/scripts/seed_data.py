from app.core.database import get_db
from app.core.security import hash_password


def run():
    db = get_db()
    users = db["users"]
    if users.count_documents({"email": "admin@healthcare.local"}) == 0:
        users.insert_one(
            {
                "name": "System Admin",
                "email": "admin@healthcare.local",
                "password": hash_password("Admin@123"),
                "role": "admin",
                "is_approved": True,
            }
        )
    print("Seed complete.")


if __name__ == "__main__":
    run()
