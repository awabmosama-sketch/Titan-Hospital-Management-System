from sqlalchemy.orm import Session
from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate, DoctorUpdate

def create_doctor(db: Session, doctor_in: DoctorCreate):
    db_doctor = Doctor(
        name=doctor_in.name,
        specialization=doctor_in.specialization,
        email=doctor_in.email,
        phone=doctor_in.phone
    )
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def get_doctor(db: Session, doctor_id: int):
    return db.query(Doctor).filter(Doctor.id == doctor_id).first()

def get_all_doctors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Doctor).offset(skip).limit(limit).all()

def update_doctor(db: Session, doctor_id: int, doctor_update: DoctorUpdate):
    db_doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not db_doctor:
        return None
    
    update_data = doctor_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_doctor, key, value)
        
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def delete_doctor(db: Session, doctor_id: int):
    db_doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not db_doctor:
        return None
    db.delete(db_doctor)
    db.commit()
    return db_doctor