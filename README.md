# Titan Hospital Management System

## 1. Overview

Titan Hospital Management System is a backend service for managing hospital operations such as doctor records, patient admissions, and staff information. The system exposes REST API endpoints built with FastAPI and uses SQLAlchemy for data persistence.

## 2. Purpose

The purpose of this system is to provide a reliable and maintainable platform for hospital administrators and medical staff to manage essential operational data efficiently.

## 3. Scope

The system covers:
- Doctor management
- Patient admission and record management
- Staff management
- API-based access to hospital data

The system does not cover billing, insurance, pharmacy, or full clinical decision support in this version.

## 4. Functional Requirements

### 4.1 Doctor Management
- Create, read, update, and delete doctor records
- Store doctor name, specialization, email, and phone

### 4.2 Patient Management
- Admit, view, update, and remove patient records
- Store patient name, age, gender, disease, admission date, and assigned doctor

### 4.3 Staff Management
- Create, read, update, and delete staff records
- Store staff name, role, department, and phone

### 4.4 API Requirements
- Provide REST endpoints for all core entities
- Validate incoming data through Pydantic schemas
- Return structured JSON responses

## 5. Non-Functional Requirements

- Performance: Fast response times for API operations
- Reliability: Consistent handling of create, read, update, and delete operations
- Maintainability: Modular structure using routes, schemas, CRUD logic, and models
- Security: Input validation and controlled access patterns
- Portability: Can be run locally with Python and a virtual environment

## 6. System Architecture

The project follows a layered architecture:

- Routes: API endpoints
- Schemas: Request and response validation
- CRUD: Business logic for database operations
- Models: SQLAlchemy database models
- Database: SQLite for local development

## 7. Technology Stack

- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- Alembic
- SQLite

## 8. Project Structure

```text
HospitalManagement/
  app/
    crud/
    models/
    routes/
    schemas/
    database.py
    main.py
  alembic/
run.py
```

## 9. Installation

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install fastapi uvicorn[standard] sqlalchemy alembic pydantic pydantic-settings psycopg2-binary python-dotenv email-validator
```

## 10. Running the Application

```bash
python run.py
```

The API will start locally and can be accessed at:

```text
http://127.0.0.1:8000
```

## 11. API Endpoints

### Doctors
- POST /doctors/
- GET /doctors/
- GET /doctors/{doctor_id}
- PUT /doctors/{doctor_id}
- DELETE /doctors/{doctor_id}

### Patients
- POST /patients/
- GET /patients/
- GET /patients/{patient_id}
- PUT /patients/{patient_id}
- DELETE /patients/{patient_id}

### Staff
- POST /staff/
- GET /staff/
- GET /staff/{staff_id}
- PUT /staff/{staff_id}
- DELETE /staff/{staff_id}

## 12. Database Notes

The application uses SQLite by default for local development. The database file is created automatically when the application starts.

## 13. Notes

This project is intended as a backend foundation for hospital management operations and can be extended with authentication, authorization, appointments, lab results, and billing modules.
