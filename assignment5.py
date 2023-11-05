@app.route('/customers_with_purchase_orders', methods=['GET'])
def get_customers_with_purchase_orders():
    pipeline = [
        {
            "$lookup": {
                "from": "purchase_orders",
                "localField": "customer_id",
                "foreignField": "customer_id",
                "as": "purchaseOrder"
            }
        },
        {
            "$project": {
                "customer_id": 1,
                "customer_name": 1,
                "email": 1,
                "mobile_number": 1,
                "purchaseOrder": 1
            }
        }
    ]

    result = list(customers_collection.aggregate(pipeline))

    return jsonify(result), 200
