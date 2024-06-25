from flask import Flask
from common.db import init_db

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:opa@app-db/tecsci"
    init_db(app)

    from modules.user import user_controller

    app.register_blueprint(user_controller.bp)

    return app