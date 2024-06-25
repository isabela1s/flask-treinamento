from modules.user.dto.user_create_payload import UserCreatePayload
from common.db.models import User
from typing import Union

from modules.user.user_repository import UserRepository


class UserService:
    @staticmethod
    def create_user(user_data: UserCreatePayload) -> User:
        return UserRepository.create_user(user_data)
    
    @staticmethod
    def delete_user(user_id: int) -> Union[None, str]:
        user = UserRepository.delete_user(user_id)
        if not user:
            return "Usuário não encontrado"
