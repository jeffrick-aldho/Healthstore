from bson import ObjectId
from pymongo.database import Database


class DoctorRepository:
    def __init__(self, db: Database):
        self.collection = db["doctor_profiles"]

    def create(self, payload: dict):
        result = self.collection.insert_one(payload)
        return self.get_by_id(str(result.inserted_id))

    def get_by_id(self, profile_id: str):
        return self.collection.find_one({"_id": ObjectId(profile_id)})

    def get_by_user_id(self, user_id: str):
        return self.collection.find_one({"user_id": ObjectId(user_id)})
