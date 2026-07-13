# Titan Hospital Management System

## Overview

Titan Hospital Management System is a backend API for managing hospital operations such as doctors, patients, and staff records. It is built with FastAPI, SQLAlchemy, and SQLite, and exposes REST endpoints for CRUD operations.

## Features

- Doctor management with create, read, update, and delete operations
- Patient admission and record management with optional doctor assignment
- Hospital staff management with create, read, update, and delete operations
- Data validation using Pydantic schemas
- SQLite persistence with a configurable database path
- Docker support for containerized deployment

## Technology Stack

- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- SQLite
- Alembic

## Project Structure

```text
HospitalManagement/
  app/
    crud/
      doctor.py
      patient.py
      staff.py
    models/
      doctor.py
      patient.py
      staff.py
    routes/
      doctor.py
      patient.py
      staff.py
    schemas/
      doctor.py
      patient.py
      staff.py
    database.py
    main.py
  alembic/
Dockerfile
README.md
requirements.txt
run.py
docker-compose.yml
```

## Models and Schemas

### Doctor
- id
- name
- specialization
- email
- phone

### Patient
- id
- name
- age
- gender
- disease
- admission_date
- doctor_id (optional)

### Staff
- id
- name
- role
- department
- phone

## API Endpoints

### Doctors
- `POST /doctors/`
- `GET /doctors/`
- `GET /doctors/{doctor_id}`
- `PUT /doctors/{doctor_id}`
- `DELETE /doctors/{doctor_id}`

### Patients
- `POST /patients/`
- `GET /patients/`
- `GET /patients/{patient_id}`
- `PUT /patients/{patient_id}`
- `DELETE /patients/{patient_id}`

### Staff
- `POST /staff/`
- `GET /staff/`
- `GET /staff/{staff_id}`
- `PUT /staff/{staff_id}`
- `DELETE /staff/{staff_id}`

## Local Setup

1. Clone the repository.
2. Create and activate a virtual environment.

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies.

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run Locally

Use the launcher script:

```bash
python run.py
```

By default this script starts the app on `0.0.0.0` and selects an available port if `PORT` is not set. If binding to `0.0.0.0` does not work on your machine, use `127.0.0.1` instead.

To bind to a fixed port:

```bash
set PORT=8000
python run.py
```

Or run Uvicorn directly from the repository root:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --app-dir HospitalManagement
```

If `0.0.0.0` fails, run:

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --app-dir HospitalManagement
```

## Docker

Build and run with Docker Compose:

```bash
docker compose up --build
```

The service is exposed on host port `8080` by default.

## Database

The application uses SQLite by default. The database file is created automatically when the app starts.

Default path:

```text
HospitalManagement/hospital.db
```

Override the database file location using the `DB_PATH` environment variable.

## Notes

- The root endpoint `/` returns a simple status message to confirm the backend is online.
- This repository is a backend foundation and can be extended with authentication, appointment scheduling, billing, and additional hospital workflows.
