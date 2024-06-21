from flask import Flask
from common.db import init_db, db
from web.common.db.models import User

def create_app() -> Flask:
    app = Flask(__name__)
    init_db(app)

    @app.get("/users")
    def list_users():
        users = db.session.query(User).all()
        return [{"id": u.id, "name": u.name} for u in users]
    return app