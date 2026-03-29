from app.core.database import get_db
from app.repositories.doctor_repository import DoctorRepository
from app.repositories.user_repository import UserRepository
from app.schemas.doctor_schema import DoctorProfileCreate
from app.services.doctor_service import DoctorService
from app.utils.helpers import serialize_doc


def create_doctor_profile_controller(user: dict, payload: DoctorProfileCreate):
    service = DoctorService(DoctorRepository(get_db()), UserRepository(get_db()))
    return serialize_doc(service.create_profile(str(user["_id"]), payload))
