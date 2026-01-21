import requests
from sqlalchemy.dialects.postgresql import insert
from models.customer import Customer

FLASK_API_URL = "http://mock-server:5000/api/customers"


def ingest_customers(db):
    page = 1
    limit = 10
    total_processed = 0

    while True:
        response = requests.get(FLASK_API_URL, params={"page": page, "limit": limit})
        response.raise_for_status()

        payload = response.json()
        data = payload.get("data", [])

        if not data:
            break

        for customer in data:
            stmt = insert(Customer).values(**customer)
            stmt = stmt.on_conflict_do_update(
                index_elements=["customer_id"], set_=customer
            )
            db.execute(stmt)
            total_processed += 1

        db.commit()

        if page * limit >= payload["total"]:
            break

        page += 1

    return total_processed
