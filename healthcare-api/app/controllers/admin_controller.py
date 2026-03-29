from app.core.database import get_db
from app.repositories.doctor_repository import DoctorRepository
from app.repositories.user_repository import UserRepository
from app.services.doctor_service import DoctorService
from app.services.user_service import UserService
from app.utils.helpers import serialize_doc


def users_controller():
    service = UserService(UserRepository(get_db()))
    return [serialize_doc(item) for item in service.list_users()]


def delete_user_controller(user_id: str):
    service = UserService(UserRepository(get_db()))
    return {"deleted": service.delete_user(user_id)}


def approve_doctor_controller(user_id: str):
    service = DoctorService(DoctorRepository(get_db()), UserRepository(get_db()))
    return serialize_doc(service.approve_doctor(user_id))


def reports_controller():
    users = UserRepository(get_db()).list_all()
    appointments_count = get_db()["appointments"].count_documents({})
    prescriptions_count = get_db()["prescriptions"].count_documents({})
    return {
        "users_total": len(users),
        "appointments_total": appointments_count,
        "prescriptions_total": prescriptions_count,
    }
