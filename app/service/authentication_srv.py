# -*- coding: utf-8 -*-
import datetime

from werkzeug.security import check_password_hash

from app import constant
from app.exception import BusinessException, AuthenticationException, InternalException
from app.util import jwt_util
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


def verify_token(token):
    _token = str.strip(token)
    if not _token:
        raise AuthenticationException(message='令牌缺失', status=constant.BLANK_TOKEN)
    try:
        payload = jwt_util.decode_auth_token(_token)
    except InternalException as e:
        raise AuthenticationException(message=e.message, status=constant.INVALID_TOKEN)
    if not jwt_util.is_valid_token(payload):
        raise AuthenticationException(message='令牌无效', status=constant.INVALID_TOKEN)
    if jwt_util.is_token_expired(payload['exp']):
        raise AuthenticationException(message='令牌过期', status=constant.EXPIRED_TOKEN)
    return True
