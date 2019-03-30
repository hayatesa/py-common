from uuid import uuid1
from app.vo.UserVO import UserVO
from app.dao.UserDAO import user_dao
from . import session_commit


class UserService:

    @staticmethod
    def find_list():
        return user_dao.list()

    @staticmethod
    def find_page():
        return

    @staticmethod
    def find_by_id(user_id):
        return user_dao.find(user_id)

    @staticmethod
    def find_by_username(username):
        users = user_dao.find_by_username(username)
        if not users:
            return None
        return users[0]

    @staticmethod
    def update(user):
        user_dao.update(user)
        session_commit()

    @staticmethod
    def add(user):
        user.id = uuid1()
        user_dao.add(user)
        session_commit()

    @staticmethod
    def delete(user_id):
        user = user_dao.find(user_id)
        if not user:
            return
        user.isDeleted = 1
        user_dao.add(user)
        session_commit()
        return user


user_service = UserService()
