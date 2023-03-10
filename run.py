from src import UserRepo
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return 'Olá estou online'

@app.route("/insert", methods=["POST"])
def insert():
    userRep = UserRepo()
    body = request.json

    userRep.insert_user(body["name"], body["age"])

    return 'OK'

@app.route("/read", methods=["GET"])
def read():
    UserRep = UserRepo()
    body = request.json

    user = UserRep.read_user(body["name"])

    # Check if user exists
    if user:
        # Convert user object to dictionary
        user_dict = user.__dict__
        # Remove unnecessary attributes
        user_dict.pop("_sa_instance_state", None)
        # Return user data as JSON response
        return jsonify(user_dict)
    else:
        return jsonify({"message": "User not found"})