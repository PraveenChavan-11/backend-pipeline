from flask import Flask, jsonify, request, abort
import json
import os

app = Flask(__name__)

# Load customers from JSON file
DATA_FILE = os.path.join("data", "customers.json")

with open(DATA_FILE, "r") as f:
    customers = json.load(f)


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/api/customers", methods=["GET"])
def get_customers():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    # Pagination logic
    offset = (page - 1) * limit
    paginated_customers = customers[offset : offset + limit]

    return (
        jsonify(
            {
                "data": paginated_customers,
                "total": len(customers),
                "page": page,
                "limit": limit,
            }
        ),
        200,
    )


@app.route("/api/customers/<customer_id>", methods=["GET"])
def get_customer_by_id(customer_id):
    for customer in customers:
        if customer["customer_id"] == customer_id:
            return jsonify(customer), 200

    abort(404, description="Customer not found")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
