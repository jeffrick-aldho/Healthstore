from bson import ObjectId


def new_doctor_profile(user_id: str, specialization: str, experience: int, availability: list[str]) -> dict:
    return {
        "user_id": ObjectId(user_id),
        "specialization": specialization,
        "experience": experience,
        "availability": availability,
    }
