from src import UserRepo
from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return 'Olá estou online'

@app.route("/insert", methods=["POST"])
def insert():
    userRepo = UserRepo()
    body = request.json

    userRepo.insert_user(body["name"], body["age"])

    return 'OK'

@app.route("/read", methods=["GET"])
def read():
    UserRepo = UserRepo()
    body = request.json

    UserRepo.read_user(body["name"])

    return 'OK'