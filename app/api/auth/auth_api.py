# -*- coding: utf-8 -*-
import traceback

from flask import request

from app import constant
from app.exception import ParameterException
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
        raise ParameterException(message='Parameter should not be blank.', status=constant.FAILURE_STATUS)
    if not (data and data.get('token') and str.strip(data.get('token'))):
        raise ParameterException(message='Parameter \'token\' should not be blank.', status=constant.BLANK_TOKEN)
    authentication_srv.verify_token(data['token'])
    return success()
