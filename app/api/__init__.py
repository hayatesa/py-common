# -*- coding: utf-8 -*-
"""API全局控制"""
import traceback

from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask import request
from app import app, APPLICATION_CONFIG
from app.exception import AuthenticationError, AuthorizationError, ServiceError, ParameterInvalidError, InternalError
from app.service.authentication_srv import verify_password as verify_pwd, verify_token as verify_tk
from app import logger
from app.util.resp import error
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
        raise ParameterInvalidError(description='请提供用户名')
    if not _password:
        raise ParameterInvalidError(description='请提供密码')
    return verify_pwd(_username, _password)


@token_auth.verify_token
def verify_token(token):
    return verify_tk(token)


# 全局异常处理
@app.errorhandler(400)
def bad_request(e):
    logger.error(traceback.format_exc())
    return error(status=400, description=e.description, http_status=400)


@app.errorhandler(401)
def unauthorized(e):
    logger.error(traceback.format_exc())
    return error(status=401, description=e.description, http_status=401)


@app.errorhandler(403)
def forbidden(e):
    logger.error(traceback.format_exc())
    return error(status=403, description=e.description, http_status=403)


@app.errorhandler(404)
def not_found(e):
    logger.error(traceback.format_exc())
    return error(status=404, description=e.description, http_status=404)


@app.errorhandler(405)
def method_not_allowed(e):
    logger.error(traceback.format_exc())
    return error(status=405, description=e.description, http_status=405)


@app.errorhandler(500)
def internal_server_error(e):
    logger.error(traceback.format_exc())
    return error(status=500, description=e.description, http_status=500)


@app.errorhandler(ParameterInvalidError)
def parameter_error_handler(e):
    logger.error(traceback.format_exc())
    return error(status=constant.BAD_REQUEST, description=e.description,
                 fields=e.fields if hasattr(list, 'fields') else None, http_status=400)


@app.errorhandler(AuthenticationError)
def authentication_error_handler(e):
    logger.error(traceback.format_exc())
    return error(status=constant.INVALID_TOKEN, description=e.description, http_status=401)


@app.errorhandler(AuthorizationError)
def authorization_error_handler(e):
    logger.error(traceback.format_exc())
    return error(status=constant.FORBIDDEN, description=e.description, http_status=403)


@app.errorhandler(ServiceError)
def service_error_handler(e):
    logger.error(traceback.format_exc())
    return error(status=constant.SERVICE_ERROR, description=e.description, http_status=200)


@app.errorhandler(InternalError)
def internal_error_handler(e):
    logger.error(traceback.format_exc())
    return error(description=e.description, http_status=constant.INTERNAL_ERROR)


@app.errorhandler(Exception)
def error_handler(e):
    logger.error(traceback.format_exc())
    return error(description='Internal Server Error: %s' % str(e) or 'Unknown Error.',
                 http_status=constant.INTERNAL_ERROR)
