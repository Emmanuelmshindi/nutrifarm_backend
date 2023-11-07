from backend.models.engine.database import app, db


def create_tables():
    with app.app_context():
        db.create_all()
