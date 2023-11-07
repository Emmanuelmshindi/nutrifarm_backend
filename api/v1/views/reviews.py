from flask import request
from backend.models.review import Review
from backend.models.engine.db_storage import db
from datetime import datetime
from backend.api.v1.views import app_views


def format_review(review):
    return {
        "user_id": review.user_id,
        "content": review.content,
        "created_at": review.created_at,
    }


# Create a review
@app_views.route("/reviews", methods=["POST"], strict_slashes=False)
def create_review():
    user = request.json["user_id"]
    content = request.json["content"]
    review = Review(user, content)
    db.session.add(review)
    db.session.commit()
    return format_review(review)


# Get all reviews
@app_views.route("/reviews", methods=["GET"], strict_slashes=False)
def get_reviews():
    reviews = Review.query.order_by(Review.id.asc()).all()
    review_list = []
    for review in reviews:
        review_list.append(review)
    return {"reviews": review_list}


# Get single review
@app_views.route("/reviews/<id>", methods=["GET"], strict_slashes=False)
def get_review(id):
    review = Review.query.filter_by(id=id).one()
    formatted_review = format_review(review)
    return formatted_review


# Delete a review
@app_views.route("/reviews/<id>", methods=["DELETE"], strict_slashes=False)
def delete_review(id):
    review = Review.query.filter_by(id=id).one()
    db.session.delete(review)
    db.session.commit()
    return f"Review {review.id} deleted!"


# Edit a review
@app_views.route("/reviews/<id>", methods=["PUT"], strict_slashes=False)
def edit_review(id):
    review = Review.query.filter_by(id=id)
    content = request.json["content"]
    review.update(dict(content=content, updated_at=datetime.utcnow))
    db.session.commit()
    return {"review": format_review(review.one())}
