from src import UserRepo
from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return 'Olá estou online'

@app.route("/insert", methods=["POST"])
def insert():
    import logging
    logger=logging.getLogger()
    logger.error('CHEGOU AQUI')
    userRepo = UserRepo()
    body = request.json

    userRepo.insert_user(body["name"])

    return 'OK'