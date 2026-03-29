from fastapi import APIRouter, Depends

from app.controllers.patient_controller import patient_profile_controller
from app.core.dependencies import require_roles

router = APIRouter()


@router.get("/me")
def my_profile(user: dict = Depends(require_roles("patient"))):
    return patient_profile_controller(user)
