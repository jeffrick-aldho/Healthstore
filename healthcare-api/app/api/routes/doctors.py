from fastapi import APIRouter, Depends

from app.controllers.doctor_controller import create_doctor_profile_controller
from app.core.dependencies import require_roles
from app.schemas.doctor_schema import DoctorProfileCreate

router = APIRouter()


@router.post("/profile")
def create_profile(payload: DoctorProfileCreate, user: dict = Depends(require_roles("doctor"))):
    return create_doctor_profile_controller(user, payload)
