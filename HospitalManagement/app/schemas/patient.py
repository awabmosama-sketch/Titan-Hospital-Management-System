from pydantic import BaseModel
from datetime import date
from typing import Optional

class PatientBase(BaseModel):
    name            : str
    age             : int
    gender          : str
    disease         : str
    addmission_date : date


class PatientCreate(PatientBase):
    doctor_id : Optional[int] = None


class PatientUpdate(BaseModel):
    name            : Optional[str] = None
    age             : Optional[int] = None
    gender          : Optional[str] = None
    disease         : Optional[str] = None
    admission_date  : Optional[date] = None
    doctor_id       : Optional[int] = None

class PatientResponse(PatientBase):
    id : int
    doctor_id = Optional[int] = None

    class Config:
        from_attributes = True
