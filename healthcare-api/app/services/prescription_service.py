from bson import ObjectId
from fastapi import HTTPException

from app.models.prescription_model import new_prescription
from app.repositories.appointment_repository import AppointmentRepository
from app.repositories.prescription_repository import PrescriptionRepository
from app.schemas.prescription_schema import PrescriptionCreate


class PrescriptionService:
    def __init__(
        self,
        prescription_repo: PrescriptionRepository,
        appointment_repo: AppointmentRepository,
    ):
        self.prescription_repo = prescription_repo
        self.appointment_repo = appointment_repo

    def create(self, doctor_id: str, payload: PrescriptionCreate):
        appointment = self.appointment_repo.get_by_id(payload.appointment_id)
        if not appointment:
            raise HTTPException(status_code=404, detail="Appointment not found")
        if str(appointment["doctor_id"]) != doctor_id:
            raise HTTPException(status_code=403, detail="Cannot prescribe for this appointment")

        model = new_prescription(
            appointment_id=payload.appointment_id,
            doctor_id=doctor_id,
            notes=payload.notes,
            medicines=[m.model_dump() for m in payload.medicines],
        )
        return self.prescription_repo.create(model)

    def list_for_patient(self, patient_id: str):
        appointments = self.appointment_repo.get_by_patient(patient_id)
        appointment_ids = [a["_id"] for a in appointments]
        if not appointment_ids:
            return []
        return self.prescription_repo.get_by_patient_appointments([aid if isinstance(aid, ObjectId) else ObjectId(aid) for aid in appointment_ids])
