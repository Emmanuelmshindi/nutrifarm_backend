from flask import request
from backend.models.meal import Meal
from backend.models.engine.db_storage import db
from datetime import datetime
from backend.api.v1.views import app_views


def format_meal(meal):
    return {
        "id": meal.id,
        "plan_id": meal.plan_id,
        "day": meal.day,
        "meal1": meal.meal1,
        "meal2": meal.meal2,
        "description": meal.description,
        "created_at": meal.created_at,
    }


# Create a meal
@app_views.route("/<plan_id>/meals", methods=["POST"])
def create_meal(plan_id):
    plan_id = request.json["plan_id"]
    day = request.json["day"]
    meal1 = request.json["meal1"]
    meal2 = request.json["meal2"]
    description = request.json["description"]
    meal = Meal(plan_id, day, meal1, meal2, description)
    db.session.add(meal)
    db.session.commit()
    return format_meal(meal)


# Get all meals in a plan
@app_views.route("/<plan_id>/meals", methods=["GET"], strict_slashes=False)
def get_meals(plan_id):
    meals = Meal.query.order_by(Meal.id.asc()).all()
    meal_list = []
    for meal in meals:
        meal_list.append(format_meal(meal))
    return {"meals": meal_list}


# Get a single day's meal in a specific plan
@app_views.route("/<plan_id>/meals/<id>", methods=["GET"], strict_slashes=False)
def get_meal(id):
    day_meal = Meal.query.filter_by(id=id).one()
    formatted_meal = format_meal(day_meal)
    return {"Meals today": formatted_meal}


# Delete a meal
@app_views.route("/<plan_id>/meals/<id>", methods=["DELETE"], strict_slashes=False)
def delete_meal(id):
    day_meal = Meal.query.filter_by(id=id).one()
    db.session.delete(day_meal)
    db.session.commit()
    return f"{Meal.day}'s meal deteled!"


# Edit a day's meal
@app_views.route("/<plan_id>/meals/<id>", methods=["PUT"], strict_slashes=False)
def update_meal(id):
    day_meal = Meal.query.filter_by(id=id)
    plan_id = request.json["plan_id=plan_id"]
    day = request.json["day"]
    meal1 = request.json["meal1"]
    meal2 = request.json["meal2"]
    description = request.json["description"]
    day_meal.update(
        dict(
            plan_id=plan_id,
            day=day,
            meal1=meal1,
            meal2=meal2,
            description=description,
            updated_at=datetime.utcnow,
        )
    )
    return {"meal": format_meal(day_meal.one())}
