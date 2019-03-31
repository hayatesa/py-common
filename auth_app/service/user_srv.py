# -*- coding: utf-8 -*-
from uuid import uuid1
from auth_app.dao.user_dao import user_dao
from auth_app.service import session_commit


def find_list():
    return user_dao.list()


def find_page():
    return


def find_by_id(user_id):
    return user_dao.find(user_id)


def find_by_username(username):
    users = user_dao.find_by_username(username)
    if not users:
        return None
    return users[0]


def update(user):
    user_dao.update(user)
    session_commit()


def add(user):
    user.id = uuid1()
    user_dao.add(user)
    session_commit()


def delete(user_id):
    user = user_dao.find(user_id)
    if not user:
        return
    user.isDeleted = 1
    user_dao.add(user)
    session_commit()
    return user
