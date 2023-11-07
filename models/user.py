from backend.models.engine.db_storage import db
from backend.models.base_model import BaseModel, Base


class User(BaseModel, Base, db.Model):
    __tablename__ = "users"
    username = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    phone_number = db.Column(db.Integer, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    health_status = db.Column(db.String(60), nullable=True)
    user_reviews = db.relationship("Review", backref="user_reviews")

    def __repr__(self):
        return f"Name: {self.usernamename}, Email: {self.email}, Password: {self.password}, Phone number: {self.phone_number}, Age: {self.age}, Health Status: {self.health_status}"

    def __init__(
        self, username, email, password, phone_number, age, health_status, user_reviews
    ):
        self.username = username
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.age = age
        self.health_status = health_status
        self.user_reviews = user_reviews
