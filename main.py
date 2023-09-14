from flask import Flask, request, jsonify
import pymongo
from gridfs import GridFS
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or get the database
db = client["everybar"]

# Create or get a collection (similar to a table in SQL)
users = db["users"]
businesses = db['businesses']


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    id = data.get('uid')
    email = data.get('email')

    if id and email:
        print("in if")
        user = {"id": id, "email": email, "searches": []}
        users.insert_one(user)
        return jsonify({"message": "User added successfully"}), 200
    else:
        print("in else")
        return jsonify({"message": "Invalid data"}), 400


@app.route('/get_user', methods=['GET'])
def get_user():
    user_id = request.args.get('uid')  # Assuming 'uid' is the parameter you use to identify users

    if user_id:
        user = users.find_one({"id": user_id})
        if user:
            return jsonify(user), 200
        else:
            return jsonify({"message": "User not found"}), 404
    else:
        return jsonify({"message": "Invalid request, provide a user id"}), 400


@app.route('/add_business', methods=['POST'])
def add_business():
    expected_fields = [
        'name', 'phone', 'smoke', 'ratingAvg',
        'loud', 'openTime', 'closedTime', 'location', 'hasHappyHour',
        'menu', 'age', 'hasFood', 'isKosher'
    ]
    data = request.json
    myBusiness = data.get('business')

    with open(myBusiness['imageUrl'], 'rb') as image_file:
        image_data = image_file.read()
    with open(myBusiness['logoUrl'], 'rb') as image_file:
        logo_data = image_file.read()

    business_data = {}
    for field in expected_fields:
        value = myBusiness[field]
        if value is not None:
            business_data[field] = value
        else:
            return jsonify({"message": f"Missing data for field: {field}"}), 400

    business_data['image'] = image_data
    business_data['logo'] = logo_data

    businesses.insert_one(business_data)

    # Return success message
    return jsonify({"message": "Business added successfully"}), 200


@app.route('/get_all_businesses', methods=['GET'])
def get_all_businesses():
    try:
        # Find all businesses in the database
        all_businesses = list(businesses.find({}))
        return jsonify(all_businesses), 200

    except Exception as e:
        return jsonify({"message": f"Error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    app.run()
