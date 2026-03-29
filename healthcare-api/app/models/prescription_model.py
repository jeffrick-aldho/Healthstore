from bson import ObjectId


def new_prescription(appointment_id: str, doctor_id: str, notes: str, medicines: list[dict]) -> dict:
    return {
        "appointment_id": ObjectId(appointment_id),
        "doctor_id": ObjectId(doctor_id),
        "notes": notes,
        "medicines": medicines,
    }
