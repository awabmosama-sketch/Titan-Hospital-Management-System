from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.doctor import DoctorCreate, DoctorUpdate, DoctorResponse
from app.crud import doctor as crud_doctor

router = APIRouter(prefix="/doctors", tags=["Doctors"])

@router.post("/", response_model=DoctorResponse, status_code=status.HTTP_201_CREATED)
def add_doctor(doctor_in: DoctorCreate, db: Session = Depends(get_db)):
    return crud_doctor.create_doctor(db=db, doctor_in=doctor_in)

@router.get("/{doctor_id}", response_model=DoctorResponse)
def read_doctor(doctor_id: int, db: Session = Depends(get_db)):
    db_doctor = crud_doctor.get_doctor(db=db, doctor_id=doctor_id)
    if not db_doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return db_doctor

@router.get("/", response_model=List[DoctorResponse])
def read_all_doctors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_doctor.get_all_doctors(db=db, skip=skip, limit=limit)

@router.put("/{doctor_id}", response_model=DoctorResponse)
def modify_doctor(doctor_id: int, doctor_update: DoctorUpdate, db: Session = Depends(get_db)):
    updated = crud_doctor.update_doctor(db=db, doctor_id=doctor_id, doctor_update=doctor_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return updated

@router.delete("/{doctor_id}")
def remove_doctor(doctor_id: int, db: Session = Depends(get_db)):
    deleted = crud_doctor.delete_doctor(db=db, doctor_id=doctor_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return {"message": "Doctor successfully removed from system database"}