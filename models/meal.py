from backend.models.engine.db_storage import db
from backend.models.base_model import BaseModel, Base


class Meal(BaseModel, Base, db.Model):
    __tablename__ = "meals"
    plan_id = db.Column(db.String(36), db.ForeignKey("plans.id"), nullable=False)
    day = db.Column(db.String(20), nullable=False)
    meal1 = db.Column(db.String(100), nullable=False)
    meal2 = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Day: {self.day}, Meal1: {self.meal1}, Meal2: {self.meal2}, Description: {self.description} Plan_id: {self.plan_id}"

    def __init__(self, day, meal1, meal2, description, plan_id):
        self.day = day
        self.meal1 = meal1
        self.meal2 = meal2
        self.description = description
        self.plan_id = plan_id
