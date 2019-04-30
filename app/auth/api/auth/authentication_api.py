# -*- coding: utf-8 -*-

from flask import request
from app.auth.service import authentication_srv
from app.common.util.resp import success
from app.common.util.header_util import get_token_in_header
from app.auth.api import basic_auth
from app.auth.api import token_auth
from app.auth.api.auth import auth_bp as api


@api.route('/login', methods=['POST'])
@basic_auth.login_required
def login():
    username_auth = request.authorization.get('username') if request.authorization else None
    username = username_auth or request.json['username']
    return success(data=authentication_srv.login(username))


@api.route('/refresh-token', methods=['GET'])
@token_auth.login_required
def refresh_token():
    return success(data=authentication_srv.refresh_token(get_token_in_header()))


@api.route('/logout', methods=['GET'])
@token_auth.login_required
def logout():
    authentication_srv.logout(get_token_in_header())
    return success()


@api.route('/verify', methods=['GET'])
def verify():
    authentication_srv.verify_token(get_token_in_header())
    return success()
