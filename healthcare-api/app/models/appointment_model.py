from bson import ObjectId


def new_appointment(patient_id: str, doctor_id: str, appointment_time) -> dict:
    return {
        "patient_id": ObjectId(patient_id),
        "doctor_id": ObjectId(doctor_id),
        "appointment_time": appointment_time,
        "status": "booked",
    }
