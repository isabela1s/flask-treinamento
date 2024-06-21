from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import DBBaseModel, User

db = SQLAlchemy(model_class=DBBaseModel)

def init_db(app: Flask) -> None:
    db.init_app(app)
    with app.app_context():
        db.create_all()
    _insert_admin_user_if_not_exists(db)

def _insert_admin_user_if_not_exists(db: SQLAlchemy) -> None:
    admin_exists = db.session.query(User).filter(User.name == "admin").first() is not None
    if not admin_exists:
        admin = User(name="admin")
        db.session.add(admin)
        db.session.commit()