from app.models.appointment_model import new_appointment
from app.repositories.appointment_repository import AppointmentRepository
from app.schemas.appointment_schema import AppointmentCreate


class AppointmentService:
    def __init__(self, appointment_repo: AppointmentRepository):
        self.appointment_repo = appointment_repo

    def create(self, patient_id: str, payload: AppointmentCreate):
        appointment = new_appointment(patient_id, payload.doctor_id, payload.appointment_time)
        return self.appointment_repo.create(appointment)

    def get_my_appointments(self, user_id: str, role: str):
        if role == "doctor":
            return self.appointment_repo.get_by_doctor(user_id)
        return self.appointment_repo.get_by_patient(user_id)

    def update_status(self, appointment_id: str, status: str):
        return self.appointment_repo.update_status(appointment_id, status)
