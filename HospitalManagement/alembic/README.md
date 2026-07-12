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