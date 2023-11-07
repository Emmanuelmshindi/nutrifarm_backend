from backend.models.engine.db_storage import db
from backend.models.base_model import BaseModel, Base


class Blog(BaseModel, Base, db.Model):
    __tablename__ = "blogs"
    author_name = db.Column(db.String(60), nullable=False)
    text = db.Column(db.String(1050), nullable=False)

    def __repr__(self):
        return f"Author: {self.author_name} Text: {self.text}"

    def __init__(self, author_name, text):
        self.author_name = author_name
        self.text = text
