from datetime import datetime
from pydantic import BaseModel


class AppointmentCreate(BaseModel):
    doctor_id: str
    appointment_time: datetime


class AppointmentUpdateStatus(BaseModel):
    status: str


class AppointmentOut(BaseModel):
    id: str
    patient_id: str
    doctor_id: str
    appointment_time: datetime
    status: str
