from fastapi import APIRouter

from app.api.routes import admin, appointments, auth, doctors, patients, prescriptions

api_router = APIRouter(prefix="/api")
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(patients.router, prefix="/patients", tags=["patients"])
api_router.include_router(doctors.router, prefix="/doctor", tags=["doctor"])
api_router.include_router(appointments.router, prefix="/appointments", tags=["appointments"])
api_router.include_router(prescriptions.router, prefix="/prescriptions", tags=["prescriptions"])
api_router.include_router(admin.router, prefix="/admin", tags=["admin"])
