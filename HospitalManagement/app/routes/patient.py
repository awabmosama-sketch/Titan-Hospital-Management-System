from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud import patient as crud_patient
from app.database import get_db
from app.schemas.patient import PatientCreate, PatientResponse, PatientUpdate

router = APIRouter(prefix="/patients", tags=["Patients"])


@router.post("/", response_model=PatientResponse, status_code=status.HTTP_201_CREATED)
def admit_new_patient(patient_in: PatientCreate, db: Session = Depends(get_db)):
    return crud_patient.create_patient(db=db, patient_in=patient_in)


@router.get("/{patient_id}", response_model=PatientResponse)
def read_patient_profile(patient_id: int, db: Session = Depends(get_db)):
    db_patient = crud_patient.get_patient(db=db, patient_id=patient_id)

    if not db_patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} does not exist in our systems.",
        )
    return db_patient


@router.get("/", response_model=List[PatientResponse])
def read_all_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_patient.get_all_patients(db=db, skip=skip, limit=limit)


@router.put("/{patient_id}", response_model=PatientResponse)
def update_patient_details(patient_id: int, patient_update: PatientUpdate, db: Session = Depends(get_db)):
    updated_record = crud_patient.update_patient(db=db, patient_id=patient_id, patient_update=patient_update)

    if not updated_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cannot update. Patient with ID {patient_id} not found.",
        )
    return updated_record


@router.delete("/{patient_id}", status_code=status.HTTP_200_OK)
def discharge_patient(patient_id: int, db: Session = Depends(get_db)):
    deleted_record = crud_patient.delete_patient(db=db, patient_id=patient_id)

    if not deleted_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cannot discharge. Patient with ID {patient_id} not found.",
        )
    return {"message": f"Patient profile {patient_id} successfully purged from database."}
