from datetime import datetime
from backend.models.engine.db_storage import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text

Base = declarative_base()


class BaseModel:
    id = db.Column(
        db.String(36), primary_key=True, unique=True, default=text("uuid_generate_v4()")
    )
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
