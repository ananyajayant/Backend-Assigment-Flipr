@app.route('/customers_with_shipment', methods=['GET'])
def get_customers_with_shipment():
    city = request.args.get('city')

    pipeline = [
        {
            "$match": {"city": city}
        },
        {
            "$lookup": {
                "from": "shipping_details",
                "localField": "customer_id",
                "foreignField": "customer_id",
                "as": "shipmentDetails"
            }
        },
        {
            "$project": {
                "customer_id": 1,
                "customer_name": 1,
                "email": 1,
                "mobile_number": 1,
                "city": 1,
                "shipmentDetails": 1
            }
        }
    ]

    result = list(customers_collection.aggregate(pipeline))

    return jsonify(result), 200
