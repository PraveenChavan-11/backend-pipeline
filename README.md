Backend Pipeline Project

A full-stack backend pipeline with a mock Flask API, FastAPI ingestion service, and PostgreSQL database, designed for handling customer data ingestion, pagination, and query.

Table of Contents

Project Overview

Architecture

Tech Stack

Getting Started

Available APIs

Docker Commands

Project Structure

Author

Project Overview

This project simulates a customer data ingestion pipeline:

Mock Server: A Flask-based service that provides dummy customer data.

Pipeline Service: FastAPI service that ingests customers into PostgreSQL and exposes API endpoints.

Database: PostgreSQL used to store and query customer records.

Features:

Paginated retrieval of customers

Customer details by ID

Health and ingestion endpoints

Dockerized services for environment parity

Architecture
[Mock Server (Flask)]
          |
          v
[Pipeline Service (FastAPI)]
          |
          v
[PostgreSQL Database]


Flask service provides mock customer data

FastAPI service ingests data and exposes REST API

PostgreSQL stores customer records

Tech Stack

Python 3.10

Flask (Mock server)

FastAPI (Pipeline service)

SQLAlchemy (ORM)

PostgreSQL 15

Docker & Docker Compose

Getting Started
1. Clone the Repository
git clone https://github.com/<your-username>/backend-pipeline.git
cd backend-pipeline

2. Run Services using Docker

Build and start all services:

docker compose up -d --build


Check running containers:

docker ps


Mock server → port 5000

Pipeline service → port 8000

Postgres → port 5432

3. Stop Services
docker compose down

Available APIs
Mock Server (Flask) – Port 5000

GET /api/customers?page=<int>&limit=<int>
Retrieve paginated customer list

GET /api/customers/<customer_id>
Get customer details by ID

GET /api/health
Health check for mock server

Pipeline Service (FastAPI) – Port 8000

POST /api/ingest
Ingests customers from the mock server into PostgreSQL

GET /api/customers?page=<int>&limit=<int>
Retrieve paginated customer list from database

GET /api/customers/<customer_id>
Retrieve customer details by ID from database

Docker Commands (Quick Reference)

Build & start containers:

docker compose up -d --build


Stop and remove containers:

docker compose down


View logs for a container:

docker logs -f <container_name>


Rebuild a single service:

docker compose build <service_name>
docker compose up -d <service_name>

Project Structure
backend-pipeline/
│
├── mock-server/                # Flask mock server
│   ├── app.py
│   ├── requirements.txt
│   └── data/customers.json
│
├── pipeline-service/           # FastAPI ingestion service
│   ├── main.py
│   ├── requirements.txt
│   ├── models/
│   ├── services/
│   └── database.py
│
├── docker-compose.yml
└── README.md

Author

Praveen Chavan
Full Stack Developer | Technical Team Lead
📧 praveenchavan1104@gmail.com
📱 +91 9373668855
