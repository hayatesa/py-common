# -*- coding: utf-8 -*-

from flask import request
from app.exception import ParameterInvalidError
from app.service import authentication_srv
from app.util.resp import success
from app.api import basic_auth
from app.api import token_auth
from app.api.auth import auth_bp as api


@api.route('/login', methods=['POST'])
@basic_auth.login_required
def login():
    username_auth = request.authorization.get('username') if request.authorization else None
    username = username_auth or request.json['username']
    return success(data=authentication_srv.login(username))


@api.route('/refresh-token', methods=['POST'])
@basic_auth.login_required
def refresh_token():
    try:
        data = request.json
    except Exception:
        raise ParameterInvalidError(description='请求参数缺失')
    if not (data and data.get('token') and str.strip(data.get('token'))):
        raise ParameterInvalidError(description='令牌缺失', token='Field "token" should not be blank.')
    return success(data=authentication_srv.refresh_token(data['token']))


@api.route('/logout', methods=['POST'])
@token_auth.login_required
def logout():
    return success()


@api.route('/verify', methods=['POST'])
def verify():
    r = request
    try:
        data = request.json
    except Exception:
        raise ParameterInvalidError(description='请求参数缺失')
    if not (data and data.get('token') and str.strip(data.get('token'))):
        raise ParameterInvalidError(description='令牌缺失', token='Field "token" should not be blank.')
    authentication_srv.verify_token(data['token'])
    return success()
