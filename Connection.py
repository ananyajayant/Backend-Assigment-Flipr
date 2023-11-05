from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name)

# Connect to your MongoDB instance
client = MongoClient('mongodb://localhost:27017')
db = client['your_database_name']
customers_collection = db['customers']
