from flask import Blueprint, request, jsonify
from app.models.user import User
from app.extensions.extensions import db

auth_bp = Blueprint("auth",__name__)

@auth_bp.route('/register', methods=["POST"])
def register():
    data = request.get_json()

    username = data['username']
    email = data['email']
    password = data["password"]

    user = User(username=username, email=email)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"msg: User registred Sucessucsfully"})