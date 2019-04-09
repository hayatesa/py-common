# -*- coding: utf-8 -*-
import datetime

from werkzeug.security import check_password_hash
from app.exception import ParameterInvalidError, ServiceError, AuthenticationError
from app.util import jwt_util
from app.util.redis_session import Session
from app.service import user_srv


def login(username):
    user = user_srv.find_by_username(username)
    if not user:
        raise ServiceError("用户不存在")
    # 更新登录时间
    user.lastAccessTime = datetime.datetime.now()
    user_srv.update(user)
    # 存储Token至Redis
    token = jwt_util.encode_auth_token(user.id)
    Session(user.id, token).create()
    return token


def verify_password(username, password):
    user_info = user_srv.find_by_username(username)
    if not user_info:
        raise ServiceError(description='用户不存在')
    if not check_password_hash(user_info.password, password):
        raise ServiceError(description='密码错误')
    user_info.lastAccessTime = datetime.datetime.now()
    user_srv.update(user_info)
    return True


def verify_token(token):
    """验证令牌是否合法。

    Args:
        token: 令牌(字符串)。
    Returns:
        如果验证通过，返回True。
    Raises:
        ParameterError: 令牌为空。
        AuthenticationError: 令牌解析失败或令牌过期。
    """
    check_token(token)
    return True


def refresh_token(token):
    """使用未过期的Token换取新Token。

    Args:
        token: 令牌(字符串)。
    Returns:
        新Token。
    Raises:
        ParameterError: 令牌为空。
        AuthenticationError: 令牌解析失败或令牌过期。
    """
    user_id = check_token(token)
    new_token = jwt_util.encode_auth_token(user_id)
    Session(user_id).update(new_token)
    return new_token


def check_token(token):
    """检查Token

    :param token: 令牌
    :return: 用户id
    """
    _token = str.strip(token)
    if not _token:
        raise ParameterInvalidError(description='令牌缺失', fields={'token': 'Field "token" should not be blank.'})
    try:
        payload = jwt_util.decode_auth_token(_token)
    except ServiceError as e:
        raise AuthenticationError(description=e.description)
    if jwt_util.is_token_expired(payload['exp']):
        raise AuthenticationError(description='令牌过期')
    token_in_session = Session(payload['data']['id']).read()
    if not token_in_session:
        raise AuthenticationError(description='账号登录过期或被登出')
    # Token与Session中的Token不一致
    if not _token == token_in_session:
        raise AuthenticationError(description='账号已被其它设备登出，请重新登录')
    return payload['data']['id']
