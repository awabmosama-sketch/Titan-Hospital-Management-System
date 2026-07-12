from typing import Optional

from pydantic import BaseModel, ConfigDict


class StaffBase(BaseModel):
    name: str
    role: str
    department: str
    phone: str


class StaffCreate(StaffBase):
    pass


class StaffUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    department: Optional[str] = None
    phone: Optional[str] = None


class StaffResponse(StaffBase):
    id: int
    model_config = ConfigDict(from_attributes=True)