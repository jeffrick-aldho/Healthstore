from fastapi import APIRouter, Depends

from app.controllers.admin_controller import (
    approve_doctor_controller,
    delete_user_controller,
    reports_controller,
    users_controller,
)
from app.core.dependencies import require_roles

router = APIRouter()


@router.get("/users")
def list_users(user: dict = Depends(require_roles("admin"))):
    return users_controller()


@router.delete("/users/{user_id}")
def delete_user(user_id: str, user: dict = Depends(require_roles("admin"))):
    return delete_user_controller(user_id)


@router.put("/doctors/{user_id}/approve")
def approve_doctor(user_id: str, user: dict = Depends(require_roles("admin"))):
    return approve_doctor_controller(user_id)


@router.get("/reports")
def reports(user: dict = Depends(require_roles("admin"))):
    return reports_controller()
