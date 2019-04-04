# -*- coding: utf-8 -*-
import datetime

from werkzeug.security import check_password_hash

from app.exception import BusinessError, InternalError, UnprocessableParameterError, ParameterError
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
        raise BusinessError(description='用户不存在')
    if not check_password_hash(user_info.password, password):
        raise BusinessError(description='密码错误')
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
        UnprocessableParameterError: 令牌解析失败或令牌过期。
    """
    _token = str.strip(token)
    if not _token:
        raise ParameterError(description='令牌缺失', fields={'token': 'Field \'token\' should not be blank.'})
    try:
        payload = jwt_util.decode_auth_token(_token)
    except InternalError as e:
        raise UnprocessableParameterError(description=e.description, fields={'token': '令牌解析失败'})
    if jwt_util.is_token_expired(payload['exp']):
        raise UnprocessableParameterError(description='令牌过期', fields={'token': '令牌过期'})
    return True
