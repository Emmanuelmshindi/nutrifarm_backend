from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://USERNAME:PASSWORD@HOST/DATABASE_NAME"
db = SQLAlchemy(app)
CORS(app)

if __name__ == "__main__":
    from models.blog import Blog
    from models.expert import Expert
    from models.meal import Meal
    from models.plan import Plan
    from models.review import Review
    from models.user import User
