from fastapi import APIRouter, Depends

from app.controllers.appointment_controller import (
    create_appointment_controller,
    my_appointments_controller,
    update_appointment_status_controller,
)
from app.core.dependencies import require_roles
from app.schemas.appointment_schema import AppointmentCreate, AppointmentUpdateStatus

router = APIRouter()


@router.post("")
def create_appointment(payload: AppointmentCreate, user: dict = Depends(require_roles("patient"))):
    return create_appointment_controller(user, payload)


@router.get("/my")
def my_appointments(user: dict = Depends(require_roles("patient", "doctor", "admin"))):
    return my_appointments_controller(user)


@router.put("/{appointment_id}")
def update_appointment_status(
    appointment_id: str,
    payload: AppointmentUpdateStatus,
    user: dict = Depends(require_roles("doctor")),
):
    return update_appointment_status_controller(appointment_id, payload.status)
