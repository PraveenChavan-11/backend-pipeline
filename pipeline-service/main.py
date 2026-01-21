import time
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError

from database import SessionLocal, engine, Base
from models.customer import Customer
from services.ingestion import ingest_customers

# Retry DB connection before creating tables
max_retries = 10
for i in range(max_retries):
    try:
        Base.metadata.create_all(bind=engine)
        print("Database connected successfully")
        break
    except OperationalError:
        print("Postgres not ready, retrying in 2 seconds...")
        time.sleep(2)
else:
    raise Exception("Database connection failed after multiple attempts")

app = FastAPI(title="Customer Ingestion Pipeline")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/ingest")
def ingest(db: Session = Depends(get_db)):
    count = ingest_customers(db)
    return {"status": "success", "records_processed": count}


@app.get("/api/customers")
def list_customers(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    offset = (page - 1) * limit
    customers = db.query(Customer).offset(offset).limit(limit).all()
    total = db.query(Customer).count()
    return {"data": customers, "page": page, "limit": limit, "total": total}


@app.get("/api/customers/{customer_id}")
def get_customer(customer_id: str, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter_by(customer_id=customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer
