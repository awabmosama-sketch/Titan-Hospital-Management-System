from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class DoctorBase(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    phone: str


class DoctorCreate(DoctorBase):
    pass


class DoctorUpdate(BaseModel):
    name: Optional[str] = None
    specialization: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None


class DoctorResponse(DoctorBase):
    id: int
    model_config = ConfigDict(from_attributes=True)