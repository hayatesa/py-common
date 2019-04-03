# -*- coding: utf-8 -*-
import traceback

from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask import request
from app import app, APPLICATION_CONFIG
from app.util.resp import failure
from app.exception import AuthenticationException, AuthorizationError, BusinessException, InternalException, \
    ParameterException
from app.service.authentication_srv import verify_password as verify_pwd, verify_token as verify_tk
from app import logger

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
    return verify_tk(token)


# 全局异常处理
@app.errorhandler(400)
def bad_request(error):
    logger.error(traceback.format_exc())
    return failure(message=error.description, http_status_code=error.code)


@app.errorhandler(401)
def unauthorized(error):
    logger.error(traceback.format_exc())
    return failure(message=error.description, http_status_code=error.code)


@app.errorhandler(403)
def forbidden(error):
    logger.error(traceback.format_exc())
    return failure(message=error.description, http_status_code=error.code)


@app.errorhandler(404)
def not_found(error):
    logger.error(traceback.format_exc())
    return failure(message=error.description, http_status_code=error.code)


@app.errorhandler(405)
def method_not_allowed(error):
    logger.error(traceback.format_exc())
    return failure(message=error.description, http_status_code=error.code)


@app.errorhandler(500)
def internal_server_error(error):
    logger.error(traceback.format_exc())
    return failure(message=error.description, http_status_code=error.code)


@app.errorhandler(ParameterException)
def business_exception_handler(e):
    logger.error(traceback.format_exc())
    return failure(status=e.status, message=e.message, http_status_code=400)


@app.errorhandler(AuthenticationException)
def authentication_exception_handler(e):
    logger.error(traceback.format_exc())
    return failure(message=e.message, status=e.status, http_status_code=401)


@app.errorhandler(AuthorizationError)
def authorization_exception_handler(e):
    logger.error(traceback.format_exc())
    return failure(message=e.message, http_status_code=403)


@app.errorhandler(BusinessException)
def business_exception_handler(e):
    logger.error(traceback.format_exc())
    return failure(status=e.status, message=e.message)


@app.errorhandler(InternalException)
def internal_exception_handler(e):
    logger.error(traceback.format_exc())
    return failure(message=e.message or 'Internal Server Exception: %s' % str(e) or 'Unknown Exception.', http_status_code=500)


@app.errorhandler(Exception)
def exception_handler(e):
    logger.error(traceback.format_exc())
    return failure(message='Internal Server Error: %s' % str(e) or 'Unknown Error.', http_status_code=500)
