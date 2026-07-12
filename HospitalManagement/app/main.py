import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fastapi import FastAPI  # type: ignore[import]
from app.database import engine, Base                
from app.models import doctor, patient, staff     
from app.routes import doctor as doc_routes, patient as pat_routes, staff as staff_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Titan Hospital Management System")

app.include_router(doc_routes.router)
app.include_router(pat_routes.router)
app.include_router(staff_routes.router)

@app.get("/")
def home():
    return {"status": "Titan Backend Engine Online and Tables Connected"}