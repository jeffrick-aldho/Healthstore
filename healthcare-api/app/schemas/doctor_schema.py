from pydantic import BaseModel, Field


class DoctorProfileCreate(BaseModel):
    specialization: str = Field(min_length=2, max_length=120)
    experience: int = Field(ge=0, le=80)
    availability: list[str] = []


class DoctorProfileOut(BaseModel):
    id: str
    user_id: str
    specialization: str
    experience: int
    availability: list[str]
