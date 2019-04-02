# -*- coding: utf-8 -*-
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask import request, abort
from app import app, APPLICATION_CONFIG
from app.util.resp import failure
from app.exception import AuthenticationException, AuthorizationError, BusinessException, InternalException
from app.util import jwt_util
from app.service.authentication_srv import verify_password as verify_pwd
from app import constant

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

context_path = APPLICATION_CONFIG['server'].get('context_path', '')
version = APPLICATION_CONFIG.get('version')


# 登录认证
@basic_auth.verify_password
def verify_password(username, password):
    """
    验证用户名密码
    :param username:  用户名 来自URL组件或POST请求参数
    :param password: 密码 来自URL组件或POST请求参数
    :return: boolean
    """
    data = request.json
    _username = username or data.get('username')
    _password = password or data.get('password')
    if not _username:
        raise BusinessException(message='请提供用户名')
    if not _password:
        raise BusinessException(message='请提供密码')
    return verify_pwd(_username, _password)


@token_auth.verify_token
def verify_token(token):
    if not token:
        raise AuthenticationException(message='令牌缺失', status=constant.BLANK_TOKEN)

    payload = jwt_util.decode_auth_token(token)
    if not jwt_util.is_valid_token(payload):
        raise AuthenticationException(message='令牌无效', status=constant.INVALID_TOKEN)
    if jwt_util.is_token_expired(payload['exp']):
        raise AuthenticationException(message='令牌过期', status=constant.EXPIRED_TOKEN)
    return True


# 全局异常处理
@app.errorhandler(400)
def bad_request(error):
    return failure(message=error.description, http_status_code=error.code)


@app.errorhandler(401)
def unauthorized(error):
    return failure(message=error.description, http_status_code=error.code)


@app.errorhandler(403)
def forbidden(error):
    return failure(message=error.description, http_status_code=error.code)


@app.errorhandler(404)
def not_found(error):
    return failure(message=error.description, http_status_code=error.code)


@app.errorhandler(405)
def method_not_allowed(error):
    return failure(message=error.description, http_status_code=error.code)


@app.errorhandler(500)
def internal_server_error(error):
    return failure(message=error.description, http_status_code=error.code)


@app.errorhandler(AuthenticationException)
def authentication_exception_handler(e):
    return failure(message=e.message, status=e.status, http_status_code=401)


@app.errorhandler(AuthorizationError)
def authorization_exception_handler(e):
    return failure(message=e.message, http_status_code=403)


@app.errorhandler(BusinessException)
def business_exception_handler(e):
    return failure(status=e.status, message=e.message)


@app.errorhandler(InternalException)
def internal_exception_handler():
    return failure(message='Internal Server Error.', http_status_code=500)


@app.errorhandler(Exception)
def exception_handler(e):
    print(e)
    return failure(message='Unknown Error.', http_status_code=500)
