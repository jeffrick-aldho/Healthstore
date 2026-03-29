from bson import ObjectId
from pymongo.database import Database


class UserRepository:
    def __init__(self, db: Database):
        self.collection = db["users"]

    def create(self, payload: dict):
        result = self.collection.insert_one(payload)
        return self.get_by_id(str(result.inserted_id))

    def get_by_email(self, email: str):
        return self.collection.find_one({"email": email.lower()})

    def get_by_id(self, user_id: str):
        return self.collection.find_one({"_id": ObjectId(user_id)})

    def list_all(self):
        return list(self.collection.find())

    def delete(self, user_id: str):
        return self.collection.delete_one({"_id": ObjectId(user_id)}).deleted_count > 0

    def approve_doctor(self, user_id: str):
        self.collection.update_one({"_id": ObjectId(user_id)}, {"$set": {"is_approved": True}})
        return self.get_by_id(user_id)
