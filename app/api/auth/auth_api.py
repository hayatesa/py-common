# -*- coding: utf-8 -*-
from flask import request
from app.service import user_srv
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
