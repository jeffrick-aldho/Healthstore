from pydantic import BaseModel, Field


class MedicineItem(BaseModel):
    name: str
    dosage: str
    days: int = Field(ge=1)


class PrescriptionCreate(BaseModel):
    appointment_id: str
    notes: str
    medicines: list[MedicineItem]


class PrescriptionOut(BaseModel):
    id: str
    appointment_id: str
    doctor_id: str
    notes: str
    medicines: list[MedicineItem]
