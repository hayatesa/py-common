# -*- coding: utf-8 -*-

from flask import request
from app import constant
from app.exception import ParameterError
from app.service import user_srv
from app.service import authentication_srv
from app.util.resp import success
from app.util import jwt_util
from app.api import basic_auth
from app.api import token_auth
from app.api.auth import auth_bp as api


@api.route('/token', methods=['POST'])
@basic_auth.login_required
def token():
    username_auth = request.authorization.get('username') if request.authorization else None
    user = user_srv.find_by_username(username_auth or request.json['username'])
    return success(data=jwt_util.encode_auth_token(user.id, user.username))


@api.route('/logout', methods=['POST'])
@token_auth.login_required
def logout():
    return success()


@api.route('/verify', methods=['POST'])
def verify():
    try:
        data = request.json
    except Exception:
        raise ParameterError(description='请求参数缺失')
    if not (data and data.get('token') and str.strip(data.get('token'))):
        raise ParameterError(description='令牌缺失', fields={'token': 'Field \'token\' should not be blank.'})
    authentication_srv.verify_token(data['token'])
    return success()
