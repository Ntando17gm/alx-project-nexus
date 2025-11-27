# Online Poll System Backend  
### ProDev Backend Engineering – Project Nexus

This project is a backend service for an **online poll system**, built as part of the **ProDev Backend Engineering program**. It allows users to create polls, vote, and view real-time results through well-structured APIs.

---

## Project Overview

The Online Poll System Backend simulates a real-world voting application. It focuses on:

- Building scalable and efficient APIs  
- Designing optimized database schemas  
- Preventing duplicate votes  
- Calculating real-time results  
- Documenting APIs using Swagger  

This project demonstrates core backend engineering skills in API design, database modeling, optimization, and documentation.

---

## Tech Stack

| Technology  | Purpose |
|-------------|---------|
| **Django** | Backend framework |
| **Django REST Framework** | API development |
| **PostgreSQL** | Database engine |
| **Swagger / DRF-YASG** | Interactive API documentation |
| **Docker (optional)** | Containerization |

---

## Key Features

### 1. Poll Management
- Create polls with multiple options  
- Add metadata: description, expiry date, timestamps  
- Retrieve poll details

### 2. Voting System
- Cast a vote for any poll option  
- Prevent duplicate votes using simple user validation  
- Validate poll expiry before allowing votes

### 3. Real-Time Result Computation
- Aggregate vote counts efficiently  
- Optimized queries for fast computation  
- Returns vote totals and percentages

### 4. API Documentation
- Swagger documentation available at:  

