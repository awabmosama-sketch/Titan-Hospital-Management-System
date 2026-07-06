from pydantic import BaseModel, EmailStr
from typing import Optional

class DoctorBase(BaseModel):
    name : str
    specialization : str
    email : EmailStr
    