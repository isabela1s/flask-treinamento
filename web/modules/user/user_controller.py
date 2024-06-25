from http import HTTPStatus
from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from common.db import db
from common.db.models import User
from modules.user.dto.user_create_payload import UserCreatePayload
from modules.user.user_service import UserService

# Blueprint = grupo de rotas

bp = Blueprint("users", __name__, url_prefix="/users")

def _user_to_dict(user: User):
    return {
            "id": user.id,
            "name": user.name,
            "age": user.age,
            "email": user.email,
            "password": user.password
        }

@bp.get("")
def list_users():
    users = db.session.query(User).all()
    return [_user_to_dict(u) for u in users]

@bp.post('')
def create_user():
    client_data = request.get_json()
    try:
        user_data = UserCreatePayload.model_validate(client_data)
        user = UserService.create_user(user_data)
        return  _user_to_dict(user)# retorna os dados validados como dict
    except ValidationError as e:
        response = jsonify(message=str(e))
        response.status_code = HTTPStatus.BAD_REQUEST
        return response

@bp.delete("/<int:user_id>")
def delete_user(user_id: int):
    UserService.delete_user(user_id)
    return {'message': 'Usuário deletado com sucesso'}
