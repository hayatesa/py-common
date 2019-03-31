# -*- coding: utf-8 -*-
import datetime

from werkzeug.security import check_password_hash

from app.exception import BusinessException
from app.util.redis_util import redis_util
from app.service import user_srv


def login(username, token):
    user_info = user_srv.find_by_username(username)
    # 更新登录时间
    user_info.lastAccessTime = datetime.datetime.now()
    user_srv.update(user_info)
    # 存储Token至Redis
    redis_util.client.set(username, token)


def verify_password(username, password):
    user_info = user_srv.find_by_username(username)
    if not user_info:
        raise BusinessException(message='用户不存在')
    if not check_password_hash(user_info.password, password):
        raise BusinessException(message='密码错误')
    user_info.lastAccessTime = datetime.datetime.now()
    user_srv.update(user_info)
    return True
