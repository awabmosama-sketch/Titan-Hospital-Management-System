from sqlalchemy.orm import Session
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientUpdate

def create_patient(db: Session, patient_in: PatientCreate):
    db_patient = Patient(
        name            = patient_in.name,
        age             = patient_in.age,
        gender          = patient_in.gender,
        disease         = patient_in.disease,
        admission_date  = patient_in.addmission_date,
        doctor_id       = patient_in.doctor_id
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patient(db : Session , patient_id : int):
    return db.query(Patient).filter(Patient.id == patient_id).first()


def get_all_patients(db : Session,skip:int = 0,limit : int = 100):
    return db.query(Patient).offset(skip).limit(limit).all()

def update_paitent(db : Session,patient_id : int , patient_update : PatientUpdate):
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not db_patient:
        return None
    
    update_data = patient_update.dict(exclude_unset=True)

    for key , value in update_data.items():
        setattr(db_patient,key,value)

    db.commit()
    db.refresh(db_patient)
    return db_patient

def delete_patient(db : Session,patient_id : int):
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not db_patient:
        return None

    db.delete(db_patient)
    db.commit()
    return db_patient

