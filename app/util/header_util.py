from flask import request
from app import APPLICATION_CONFIG
from app.exception import ParameterInvalidError


def get_token_in_header():
    token_in_header = request.headers.get(APPLICATION_CONFIG['jwt'].get('header_key'))
    if not token_in_header:
        raise ParameterInvalidError(description='令牌缺失', token='Field "token" should not be blank.')
    return token_in_header


def get_val_by_key(key):
    return request.headers.get(key)
