from modules.user.dto.user_create_payload import UserCreatePayload
from common.db.models import User
from common.db import db


class UserRepository:
    @staticmethod
    def create_user(user_data: UserCreatePayload) -> User:
        user = User(**user_data.model_dump()) # user = User(name=user_data.name, password=...)
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def delete_user(user_id: int):
        user = db.session.get(User, user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
