from flask import request
from backend.models.user import User
from backend.models.engine.db_storage import db
from backend.api.v1.views import app_views


def format_user(user):
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "password": user.password,
        "phone_number": user.phone_number,
        "age": user.age,
        "health_status": user.health_status,
        "user_reviews": user.user_reviews,
        "created_at": user.created_at,
    }


# Create a user
@app_views.route("/users", methods=["POST"], strict_slashes=False)
def create_user():
    username = request.json["username"]
    email = request.json["email"]
    password = request.json["password"]
    phone_number = request.json["phone_number"]
    age = request.json["age"]
    health_status = request.json["health_status"]
    user_reviews = request.json["user_reviews"]
    user = User(
        username, email, password, phone_number, age, health_status, user_reviews
    )
    db.session.add(user)
    db.session.commit()
    return format_user(user)


# Get all users
@app_views.route("/users", methods=["GET"], strict_slashes=False)
def get_users():
    users = User.query.order_by(User.id.asc()).all()
    user_list = []
    for user in users:
        user_list.append(format_user(user))
    return {"users": user_list}


# Get a single user
@app_views.route("/users/<id>", methods=["GET"], strict_slashes=False)
def get_user(id):
    user = User.query.filter_by(id=id).one()
    formatted_user = format_user(user)
    return {"user": formatted_user}


# Delete a user
@app_views.route("/users/<id>", methods=["DELETE"], strict_slashes=False)
def delete_user(id):
    user = User.query.filter_by(id=id).one()
    db.session.delete(user)
    db.session.commit()
    return f"User {user.username} deleted!"


# Edit a user
@app_views.route("/users/<id>", methods=["PUT"], strict_slashes=False)
def update_user(id):
    user = User.query.filter_by(id=id)
    username = request.json["username"]
    email = request.json["email"]
    password = request.json["password"]
    phone_number = request.json["phone_number"]
    age = request.json["age"]
    health_status = request.json["health_status"]
    user_reviews = request.json["user_reviews"]
    user = User(
        username, email, password, phone_number, age, health_status, user_reviews
    )
    user.update(
        dict(
            username=username,
            email=email,
            password=password,
            phone_number=phone_number,
            age=age,
            health_status=health_status,
            user_reviews=user_reviews,
        )
    )
    db.session.commit()
    return {"user": format_user(user.one())}
