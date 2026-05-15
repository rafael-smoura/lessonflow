from flask import Blueprint, request, jsonify
from app.models.user import User
from app.extensions.extensions import db

auth_print = Blueprint("auth",__name__)

@auth_print('/register', methods=["POST"])
def register():
    data = request.get_json()

    username = data['username']
    email = data['email']
    password = data["passowrd"]

    user = User(username=username, email=email)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"msg: User registred Sucessucsfully"})