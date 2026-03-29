from app.core.database import get_db
from app.repositories.appointment_repository import AppointmentRepository
from app.repositories.prescription_repository import PrescriptionRepository
from app.schemas.prescription_schema import PrescriptionCreate
from app.services.prescription_service import PrescriptionService
from app.utils.helpers import serialize_doc


def create_prescription_controller(user: dict, payload: PrescriptionCreate):
    service = PrescriptionService(PrescriptionRepository(get_db()), AppointmentRepository(get_db()))
    created = service.create(str(user["_id"]), payload)
    return serialize_doc(created)


def my_prescriptions_controller(user: dict):
    service = PrescriptionService(PrescriptionRepository(get_db()), AppointmentRepository(get_db()))
    records = service.list_for_patient(str(user["_id"]))
    return [serialize_doc(item) for item in records]
