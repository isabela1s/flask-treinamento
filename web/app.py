from flask import Flask
from common.db import init_db, db
from common.db.models import User

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:opa@app-db/tecsci"
    init_db(app)

    @app.get("/users")
    def list_users():
        users = db.session.query(User).all()
        return [{"id": u.id, "name": u.name} for u in users]
    return app