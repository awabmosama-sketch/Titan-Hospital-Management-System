from sqlalchemy.orm import Session
from app.models.staff import Staff
from app.schemas.staff import StaffCreate, StaffUpdate

def create_staff(db: Session, staff_in: StaffCreate):
    db_staff = Staff(
        name=staff_in.name,
        role=staff_in.role,
        department=staff_in.department,
        phone=staff_in.phone
    )
    db.add(db_staff)
    db.commit()
    db.refresh(db_staff)
    return db_staff

def get_staff(db: Session, staff_id: int):
    return db.query(Staff).filter(Staff.id == staff_id).first()

def get_all_staff(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Staff).offset(skip).limit(limit).all()

def update_staff(db: Session, staff_id: int, staff_update: StaffUpdate):
    db_staff = db.query(Staff).filter(Staff.id == staff_id).first()
    if not db_staff:
        return None
        
    update_data = staff_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_staff, key, value)
        
    db.commit()
    db.refresh(db_staff)
    return db_staff

def delete_staff(db: Session, staff_id: int):
    db_staff = db.query(Staff).filter(Staff.id == staff_id).first()
    if not db_staff:
        return None
    db.delete(db_staff)
    db.commit()
    return db_staff