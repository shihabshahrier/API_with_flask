from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import uuid
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)


@app.route("/get-user/<username>", methods=["GET"])
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({"username": user.username, "email": user.email}), 200
    else:
        return jsonify({"message": "User not found"}), 404


@app.route("/add-user", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data or "username" not in data or "email" not in data:
        return jsonify({"message": "Bad request, username and email are required"}), 400

    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"message": "Username already exists"}), 409
    print(data["username"])
    new_user = User(
        id=str(uuid.uuid4()), username=data["username"], email=data["email"]
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "New user created"}), 201


@app.route("/update/<username>", methods=["PUT"])
def update_user(username):
    print(username)
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    data = request.get_json()
    if not data or "email" not in data:
        return jsonify({"message": "Bad request, email is required"}), 400

    user.email = data["email"]
    db.session.commit()
    return jsonify({"message": "User updated"}), 200


@app.route("/delete/<username>", methods=["DELETE"])
def delete_user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
