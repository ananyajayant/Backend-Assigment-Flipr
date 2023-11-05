@app.route('/add_purchase_order', methods=['POST'])
def add_purchase_order():
    data = request.get_json()
    
    # Generate a unique purchase order ID
    purchase_order_id = str(uuid.uuid4())

    # Validate that Pricing is not greater than MRP
    if data["pricing"] > data["mrp"]:
        return "Pricing cannot be greater than MRP", 400

    purchase_order_data = {
        "purchase_order_id": purchase_order_id,
        "product_name": data["product_name"],
        "quantity": data["quantity"],
        "pricing": data["pricing"],
        "mrp": data["mrp"],
        "customer_id": data["customer_id"]
    }

    purchase_orders_collection.insert_one(purchase_order_data)

    return jsonify(purchase_order_data), 201
