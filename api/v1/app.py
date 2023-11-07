from backend.models.engine.database import (
    app,
    db,
)  # Import app and db from the new module
from .views import app_views

app.register_blueprint(app_views)


@app.route("/nutriplans")
def nutriplans():
    return "Nutriplans"


@app.teardown_appcontext
def close_db(error):
    """Close Storage"""
    db.session.remove()


if __name__ == "__main__":
    app.run(debug=True)
