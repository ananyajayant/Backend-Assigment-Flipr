#an API Endpoint to Add Shipping Details
@app.route('/add_shipping_details', methods=['POST'])
def add_shipping_details():
    data = request.get_json()

    # Ensure that the associated purchase order and customer IDs exist
    purchase_order_id = data["purchase_order_id"]
    customer_id = data["customer_id"]

    if not purchase_orders_collection.find_one({"purchase_order_id": purchase_order_id}):
        return "Purchase Order not found", 404

    if not customers_collection.find_one({"customer_id": customer_id}):
        return "Customer not found", 404

    shipping_details_data = {
        "address": data["address"],
        "city": data["city"],
        "pincode": data["pincode"],
        "purchase_order_id": purchase_order_id,
        "customer_id": customer_id
    }

    shipping_details_collection.insert_one(shipping_details_data)

    return jsonify(shipping_details_data), 201
