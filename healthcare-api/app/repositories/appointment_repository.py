from bson import ObjectId
from pymongo.database import Database


class AppointmentRepository:
    def __init__(self, db: Database):
        self.collection = db["appointments"]

    def create(self, payload: dict):
        result = self.collection.insert_one(payload)
        return self.get_by_id(str(result.inserted_id))

    def get_by_id(self, appointment_id: str):
        return self.collection.find_one({"_id": ObjectId(appointment_id)})

    def get_by_patient(self, patient_id: str):
        return list(self.collection.find({"patient_id": ObjectId(patient_id)}))

    def get_by_doctor(self, doctor_id: str):
        return list(self.collection.find({"doctor_id": ObjectId(doctor_id)}))

    def update_status(self, appointment_id: str, status: str):
        self.collection.update_one({"_id": ObjectId(appointment_id)}, {"$set": {"status": status}})
        return self.get_by_id(appointment_id)
