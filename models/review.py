from backend.models.engine.db_storage import db
from backend.models.base_model import BaseModel, Base


class Review(BaseModel, Base, db.Model):
    __tablename__ = "reviews"
    content = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.String(60), db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"Review: {self.content}, Review by: {self.user_id}"

    def __init__(self, user_id, content):
        self.user_id = user_id
        self.content = content
