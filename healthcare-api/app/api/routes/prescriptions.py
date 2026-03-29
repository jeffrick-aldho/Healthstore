from fastapi import APIRouter, Depends

from app.controllers.prescription_controller import create_prescription_controller, my_prescriptions_controller
from app.core.dependencies import require_roles
from app.schemas.prescription_schema import PrescriptionCreate

router = APIRouter()


@router.post("")
def create_prescription(payload: PrescriptionCreate, user: dict = Depends(require_roles("doctor"))):
    return create_prescription_controller(user, payload)


@router.get("/my")
def my_prescriptions(user: dict = Depends(require_roles("patient"))):
    return my_prescriptions_controller(user)
