from datetime import datetime
from flask import request
from backend.models.engine.db_storage import db
from backend.models.expert import Expert
from backend.api.v1.views import app_views


def format_expert(expert):
    return {
        "id": expert.id,
        "name": expert.name,
        "email": expert.email,
        "password": expert.password,
        "phone_number": expert.phone_number,
        "qualifications": expert.qualifications,
        "created_at": expert.created_at,
    }


# Create expert
@app_views.route("/experts", methods=["POST"], strict_slashes=False)
def create_expert():
    name = request.json["name"]
    email = request.json["email"]
    password = request.json["password"]
    phone_number = request.json["phone_number"]
    qualifications = request.json["qualifications"]
    expert = Expert(name, email, password, phone_number, qualifications)
    db.session.add(expert)
    db.session.commit()
    return format_expert(expert)


# Get all experts
@app_views.route("/experts", methods=["GET"], strict_slashes=False)
def get_experts():
    experts = Expert.query.order_by(Expert.id.asc()).all()
    expert_list = []
    for expert in experts:
        expert_list.append(format_expert(expert))
    return {"experts": expert_list}


# Get a single expert
@app_views.route("/experts/<id>", methods=["GET"], strict_slashes=False)
def get_expert(id):
    expert = Expert.query.filter_by(id=id).one()
    formatted_expert = format_expert(expert)
    return {"expert": formatted_expert}


# Delete an expert
@app_views.route("/experts/<id>", methods=["DELETE"], strict_slashes=False)
def delete_expert(id):
    expert = Expert.query.filter_by(id=id).one()
    db.session.delete(expert)
    db.session.commit()
    return f"Expert {Expert.id} deleted!"


# Edit an expert
@app_views.route("/experts/<id>", methods=["PUT"], strict_slashes=False)
def edit_expert(id):
    expert = Expert.query.filter_by(id=id)
    name = request.json["name"]
    email = request.json["email"]
    password = request.json["password"]
    phone_number = request.json["phone_number"]
    qualifications = request.json["qualifications"]
    expert = Expert(name, email, password, phone_number, qualifications)
    expert.update(
        dict(
            name=name,
            email=email,
            password=password,
            phone_number=phone_number,
            qualifications=qualifications,
            updated_at=datetime.utcnow,
        )
    )
    return {"expert": format_expert(expert.one())}
