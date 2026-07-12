from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.staff import StaffCreate, StaffUpdate, StaffResponse
from app.crud import staff as crud_staff

router = APIRouter(prefix="/staff", tags=["Hospital Staff"])

@router.post("/", response_model=StaffResponse, status_code=status.HTTP_201_CREATED)
def add_staff_member(staff_in: StaffCreate, db: Session = Depends(get_db)):
    return crud_staff.create_staff(db=db, staff_in=staff_in)

@router.get("/{staff_id}", response_model=StaffResponse)
def read_staff_member(staff_id: int, db: Session = Depends(get_db)):
    db_staff = crud_staff.get_staff(db=db, staff_id=staff_id)
    if not db_staff:
        raise HTTPException(status_code=404, detail="Staff member not found")
    return db_staff

@router.get("/", response_model=List[StaffResponse])
def read_all_staff(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_staff.get_all_staff(db=db, skip=skip, limit=limit)

@router.put("/{staff_id}", response_model=StaffResponse)
def modify_staff(staff_id: int, staff_update: StaffUpdate, db: Session = Depends(get_db)):
    updated = crud_staff.update_staff(db=db, staff_id=staff_id, staff_update=staff_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Staff member not found")
    return updated

@router.delete("/{staff_id}")
def remove_staff(staff_id: int, db: Session = Depends(get_db)):
    deleted = crud_staff.delete_staff(db=db, staff_id=staff_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Staff member not found")
    return {"message": "Staff member successfully removed from system"}