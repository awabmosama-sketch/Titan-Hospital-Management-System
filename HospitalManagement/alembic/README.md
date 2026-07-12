# Titan Hospital Management System Backend (SRS Documentation)

This repository hosts the production-ready REST API backend engine for the Titan Hospital Management System. This document serves as a modified Software Requirements Specification (SRS) and technical blueprint detailing the system constraints, functional capabilities, and structural architecture.

---

## 1. Introduction & Product Scope

### 1.1 Purpose
The purpose of this software engine is to provide a highly concurrent, secure, and modular data management service for hospital administration. It acts as the single source of truth for doctor allocations, patient admission tracking, and institutional staff provisioning.

### 1.2 User Classes and Characteristics
* **System Administrators:** Full administrative privileges to modify infrastructure, manage staff assignments, and audit logs.
* **Medical Staff (Doctors/Nurses):** Read/Write data privileges over patient clinical records and admission statuses.

---

## 2. System Architecture & Relational Topology

The system rejects monolithic inter-dependencies. It enforces a strict **Clean Multi-Layer Module Design** where every domain feature (Doctor, Patient, Staff) is physically partitioned into four isolated abstraction layers:

```text
[ Incoming Web Traffic ]
          │
          ▼
   1. app/routes/      (Presentation Layer / API Controllers)
          │
          ▼
   2. app/schemas/     (Application Layer / Pydantic Validation Gate)
          │
          ▼
   3. app/crud/        (Domain Logic Layer / Query Builders)
          │
          ▼
   4. app/models/      (Infrastructure Layer / SQLAlchemy Blueprint)
          │
          ▼
     [ PostgreSQL ]    (Persistence Engine / ACID Vault)
```

### 2.1 Database Entity Relationships
The relational schema maps enterprise workflows directly into database logic:
* **Doctors (1) to Patients (N):** A one-to-many structural mapping linked via a foreign key constraint (`doctor_id`).
* **Staff (Independent):** An isolated infrastructure table mapped for clinical operational roles.

---

## 3. Functional Requirements Specification (FRS)

### 3.1 Doctor Management Subsystem
* **REQ-DOC-1:** The system MUST accept new doctor profiles validating unique emails, phone strings, and medical specializations.
* **REQ-DOC-2:** The system MUST support partial or complete schema updates while dynamically discarding unprovided field forms.

### 3.2 Patient Admission Subsystem
* **REQ-PAT-1:** The system MUST log admissions capturing client age, gender vectors, baseline disease tracking, and historical date entries.
* **REQ-PAT-2:** The system MUST reject references to non-existent `doctor_id` values to prevent unassigned database orphans.

### 3.3 Staff Provisioning Subsystem
* **REQ-STF-1:** The system MUST catalog non-medical staff members assigning distinct corporate labels (e.g., Administration, ICU, Billing).

---

## 4. Non-Functional Requirements (NFR)

### 4.1 Safety and Reliability (ACID Concurrency)
The system leverages an enterprise connection pool using a context-managed generator routine (`get_db`). All database modifications are executed under strict transactional isolation boundaries (`autocommit=False`). If any operational line faults mid-execution, the entire state transitions are rolled back out of the memory cache to prevent partial state corruption.

### 4.2 Security and Validation
All structural formatting is checked out before touching the storage blocks. Network responses pass through an automated data parser engine (Pydantic), hiding internal server schemas and strictly forcing field type conversions.

---

## 5. System Environment & Technology Stack

| Component | Technical Framework | Purpose |
| :--- | :--- | :--- |
| **Language Engine** | Python 3.14+ | Execution runtime environment |
| **Web Framework** | FastAPI (ASGI Server) | High-performance asynchronous routing |
| **ORM Framework** | SQLAlchemy | Enterprise-grade SQL mapping abstraction |
| **Data Engine** | PostgreSQL | Multi-concurrency relational data storage |

---

## 6. Local Installation & Deployment Guide

### 6.1 Prerequisites
1. **PostgreSQL Instance:** Ensure a localized instance is active, hosting an empty data shell named `hospital_db`.
2. **Environment Sync:** Configure the runtime URL target array inside `app/database.py`.

### 6.2 Running the Application
To bypass localized process runtime bugs inside virtualized shell layers on Windows platforms, execute the specialized master entry program (`run.py`) mapped at the root directory:

```powershell
# Initialize environment connection dependencies
python run.py
```

Once the terminal logs verify execution, the interactive OpenAPI specification workbench maps directly to the local routing dashboard interface:
👉 **System Dashboard:** http://127.0.0.1:8000/docs
