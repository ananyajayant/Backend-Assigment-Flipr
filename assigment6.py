@app.route('/customers_with_purchase_orders_and_shipment', methods=['GET'])
def get_customers_with_purchase_orders_and_shipment():
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
            "$lookup": {
                "from": "shipment_details",
                "localField": "customer_id",
                "foreignField": "customer_id",
                "as": "shipmentDetail"
            }
        },
        {
            "$project": {
                "customer_id": 1,
                "customer_name": 1,
                "email": 1,
                "mobile_number": 1,
                "purchaseOrder": {
                    "purchaseOrderId": 1,
                    "productName": 1,
                    "quantity": 1
                },
                "shipmentDetail": {
                    "address": 1,
                    "city": 1,
                    "pincode": 1
                }
            }
        }
    ]

    result = list(customers_collection.aggregate(pipeline))

    return jsonify(result), 200
