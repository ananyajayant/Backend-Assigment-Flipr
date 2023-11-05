@app.route('/add_customer', methods=['POST'])
def add_customer():
    data = request.get_json()
    
    # Generate a unique customer ID
    customer_id = str(uuid.uuid4())

    customer_data = {
        "customer_id": customer_id,
        "customer_name": data["customer_name"],
        "email": data["email"],
        "mobile_number": data["mobile_number"],
        "city": data["city"]
    }

    customers_collection.insert_one(customer_data)

    return jsonify(customer_data), 201
