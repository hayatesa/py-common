# -*- coding: utf-8 -*-
import jwt
import datetime
import time
from auth_app import APPLICATION_CONFIG
from auth_app.exception import InternalException

SECRET_KEY = APPLICATION_CONFIG.get('secret_key', '')
TTL = APPLICATION_CONFIG['jwt'].get('ttl', 1800)
ALGORITHM = APPLICATION_CONFIG.get('algorithm', 'HS256')
TOKEN_PREFIX = ('%s ' % APPLICATION_CONFIG['jwt'].get('token_prefix')) if APPLICATION_CONFIG['jwt'].get('token_prefix') else ''


def encode_auth_token(user_id, username):
    """
    生成认证Token
    :return: token string
    """
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=TTL),
        'iat': datetime.datetime.utcnow(),
        'iss': 'dev',
        'data': {
            'id': user_id,
            'username': username
        }
    }
    return TOKEN_PREFIX + jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM).decode('utf-8')


def decode_auth_token(auth_token):
    """
    验证Token
    :param auth_token:
    :return: dict
    """
    token = extract(auth_token)
    # payload = jwt.decode(auth_token, auth_app.config.get('SECRET_KEY'), leeway=datetime.timedelta(seconds=10))
    # 取消过期时间验证
    try:
        payload = jwt.decode(token, SECRET_KEY, options={'verify_exp': False})
    except Exception:
        raise InternalException('Token解析失败')
    return payload


def is_valid_token(payload):
    return 'data' in payload and 'id' in payload['data'] and 'username' in payload['data']


def is_token_expired(expiration):
    return time.time() - expiration >= 0


def extract(token_in_header):
    if not TOKEN_PREFIX:
        return token_in_header
    if token_in_header.find(TOKEN_PREFIX) != 0:
        return token_in_header

    if not token_in_header.strip():
        raise InternalException('Authorization header cannot be blank.')

    if len(token_in_header) < len(TOKEN_PREFIX):
        raise InternalException('Invalid authorization header size.')

    return token_in_header[len(TOKEN_PREFIX):]

# encode为加密函数，decode为解密函数(HS256)

# JWT官网的三个加密参数为
# 1.header(type,algorithm)
#  {
#     "alg": "HS256",
#     "typ": "JWT"
#  }
# 2.playload(iss,sub,aud,exp,nbf,lat,jti)
#   iss: jwt签发者
#   sub: jwt所面向的用户
#   aud: 接收jwt的一方
#   exp: jwt的过期时间，这个过期时间必须要大于签发时间
#   nbf: 定义在什么时间之前，该jwt都是不可用的.
#   iat: jwt的签发时间
#   jti: jwt的唯一身份标识，主要用来作为一次性token,从而回避重放攻击。
# 3.signature
#
# jwt的第三部分是一个签证信息，这个签证信息由三部分组成：
#
#    header (base64后的)
#    payload (base64后的)
#    secret

# PyJwt官网的三个加密参数为
# jwt.encode(playload, key, algorithm='HS256')
# playload 同上,key为app的 SECRET_KEY algorithm 为加密算法

# 二者应该都可以用，但我们用的是python的 pyjwt ，那就入乡随俗吧
