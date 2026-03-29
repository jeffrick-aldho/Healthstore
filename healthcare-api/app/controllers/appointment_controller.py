from app.core.database import get_db
from app.repositories.appointment_repository import AppointmentRepository
from app.schemas.appointment_schema import AppointmentCreate
from app.services.appointment_service import AppointmentService
from app.utils.helpers import serialize_doc
from app.utils.validators import validate_appointment_status


def create_appointment_controller(user: dict, payload: AppointmentCreate):
    service = AppointmentService(AppointmentRepository(get_db()))
    created = service.create(str(user["_id"]), payload)
    return serialize_doc(created)


def my_appointments_controller(user: dict):
    service = AppointmentService(AppointmentRepository(get_db()))
    results = service.get_my_appointments(str(user["_id"]), user["role"])
    return [serialize_doc(item) for item in results]


def update_appointment_status_controller(appointment_id: str, status: str):
    validate_appointment_status(status)
    service = AppointmentService(AppointmentRepository(get_db()))
    updated = service.update_status(appointment_id, status)
    return serialize_doc(updated)
