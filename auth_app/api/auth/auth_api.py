# -*- coding: utf-8 -*-
from flask import request
from auth_app.service import user_srv
from auth_app.util.resp import success
from auth_app.util import jwt_util
from auth_app.api import basic_auth
from auth_app.api.auth import auth_bp as api


@api.route('/token', methods=['POST'])
@basic_auth.login_required
def token():
    username_auth = request.authorization.get('username') if request.authorization else None
    user = user_srv.find_by_username(username_auth or request.json['username'])
    return success(data=jwt_util.encode_auth_token(user.id, user.username))


@api.route('/logout', methods=['POST'])
def logout():
    return success()

