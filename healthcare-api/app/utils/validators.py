from fastapi import HTTPException

from app.utils.constants import APPOINTMENT_STATUSES, ROLES


def validate_role(role: str):
    if role not in ROLES:
        raise HTTPException(status_code=422, detail="Invalid role")


def validate_appointment_status(status: str):
    if status not in APPOINTMENT_STATUSES:
        raise HTTPException(status_code=422, detail="Invalid appointment status")
