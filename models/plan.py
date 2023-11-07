from backend.models.engine.db_storage import db
from backend.models.base_model import BaseModel, Base


class Plan(BaseModel, Base, db.Model):
    __tablename__ = "plans"
    plan_name = db.Column(db.String(60), nullable=False)
    plan_description = db.Column(db.String(100), nullable=False)
    plan_meals = db.relationship("Meal", backref="plan_meals")

    def __repr__(self):
        return f"Plan: {self.plan_name} Plan_meals: {self.plan_meals}"

    def __init__(self, plan_name, plan_description, plan_meals):
        self.plan_name = plan_name
        self.plan_description = plan_description
        self.plan_meals = plan_meals
