from app.models.doctor_profile_model import new_doctor_profile
from app.repositories.doctor_repository import DoctorRepository
from app.repositories.user_repository import UserRepository
from app.schemas.doctor_schema import DoctorProfileCreate


class DoctorService:
    def __init__(self, doctor_repo: DoctorRepository, user_repo: UserRepository):
        self.doctor_repo = doctor_repo
        self.user_repo = user_repo

    def create_profile(self, user_id: str, payload: DoctorProfileCreate):
        model = new_doctor_profile(
            user_id=user_id,
            specialization=payload.specialization,
            experience=payload.experience,
            availability=payload.availability,
        )
        return self.doctor_repo.create(model)

    def approve_doctor(self, user_id: str):
        return self.user_repo.approve_doctor(user_id)
