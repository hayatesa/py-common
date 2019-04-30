# -*- coding: utf-8 -*-
from flask import request
from app.auth import APPLICATION_CONFIG
from app.common.exception import ParameterInvalidError
from app.common.util.dict_util import read


def get_token_in_header():
    token_header_key = read(APPLICATION_CONFIG, 'jwt.header_key', 'Authorization')
    token_in_header = request.headers.get(token_header_key)
    if not token_in_header:
        raise ParameterInvalidError(description='令牌缺失', token='Field "token" should not be blank.')
    return token_in_header


def get_val_by_key(key):
    return request.headers.get(key)
