from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    disease: str
    admission_date: date


class PatientCreate(PatientBase):
    doctor_id: Optional[int] = None


class PatientUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    disease: Optional[str] = None
    admission_date: Optional[date] = None
    doctor_id: Optional[int] = None


class PatientResponse(PatientBase):
    id: int
    doctor_id: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)
