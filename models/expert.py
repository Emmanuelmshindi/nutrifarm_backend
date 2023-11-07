from backend.models.engine.db_storage import db
from backend.models.base_model import BaseModel, Base


class Expert(BaseModel, Base, db.Model):
    __tablename__ = "experts"
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    phone_number = db.Column(db.Integer, nullable=True)
    qualifications = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Name: {self.name} Email: {self.email} Password: {self.password} Phone Number: {self.phone_number} Qualifications: {self.qualifications}"

    def __init__(self, name, email, password, phone_number, qualifications):
        self.name = name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.qualifications = qualifications
