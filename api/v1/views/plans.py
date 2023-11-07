from flask import request
from backend.models.plan import Plan
from backend.models.engine.db_storage import db
from datetime import datetime
from backend.api.v1.views import app_views


def format_plan(plan):
    return {
        "plan_name": plan.plan_name,
        "description": plan.plan_description,
        "id": plan.id,
        "plan_meals": plan.plan_meals,
        "created_at": plan.created_at,
    }


# Create a meal plan
@app_views.route("/plans", methods=["POST"], strict_slashes=False)
def create_plan():
    plan_name = request.json["plan_name"]
    plan_description = request.json["plan_description"]
    plan_meals = request.json["plan_meals"]
    plan = Plan(plan_name, plan_description, plan_meals)
    db.session.add(plan)
    db.session.commit()
    return format_plan(plan)


# Get all meal plans
@app_views.route("/plans", methods=["GET"], strict_slashes=False)
def get_plans():
    plans = Plan.query.order_by(Plan.id.asc()).all()
    plan_list = []
    for plan in plans:
        plan_list.append(format_plan(plan))
    return {"plans": plan_list}


# Get single meal plan
@app_views.route("/plans/<id>", methods=["GET"], strict_slashes=False)
def get_plan(id):
    plan = Plan.query.filter_by(id=id).one()
    formatted_plan = format_plan(plan)
    return {"plan": formatted_plan}


# Delete a plan
@app_views.route("/plans/<id>", methods=["DELETE"], strict_slashes=False)
def delete_plan(id):
    plan = Plan.query.filter_by(id=id).one()
    db.session.delete(plan)
    db.session.commit()
    return f"Plan {plan.plan_name} deleted!"


# Edit a plan
@app_views.route("/plans/<id>", methods=["PUT"], strict_slashes=False)
def edit_plan(id):
    plan = Plan.query.filter_by(id=id)
    plan_name = request.json["plan_name"]
    plan_description = request.json["plan_description"]
    plan_meals = request.json["plan_meals"]
    plan.update(
        dict(
            plan_name=plan_name,
            plan_description=plan_description,
            plan_meals=plan_meals,
            updated_at=datetime.utcnow,
        )
    )
    db.session.commit()
    return {"plan": format_plan(plan.one())}
