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