from bson import ObjectId
from pymongo.database import Database


class PrescriptionRepository:
    def __init__(self, db: Database):
        self.collection = db["prescriptions"]

    def create(self, payload: dict):
        result = self.collection.insert_one(payload)
        return self.get_by_id(str(result.inserted_id))

    def get_by_id(self, prescription_id: str):
        return self.collection.find_one({"_id": ObjectId(prescription_id)})

    def get_by_patient_appointments(self, appointment_ids: list[ObjectId]):
        return list(self.collection.find({"appointment_id": {"$in": appointment_ids}}))
