# -*- coding: utf-8 -*-
"""API全局控制"""
import traceback

from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask import request
from app.auth import app, APPLICATION_CONFIG
from app.common.exception import AuthenticationError, AuthorizationError, ServiceError, ParameterInvalidError, InternalError
from app.auth.service.authentication_srv import verify_password as verify_pwd, verify_token as verify_tk
from app.auth import logger
from app.common.util.resp import error
from app.common.util.dict_util import read
from app.auth import constant

context_path = read(APPLICATION_CONFIG, 'server.context_path', '')

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


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
        raise ParameterInvalidError(description='"username" should not be blank.', username='Should not be blank.')
    if not _password:
        raise ParameterInvalidError(description='"password" should not be blank.', password='Should not be blank.')
    return verify_pwd(_username, _password)


@token_auth.verify_token
def verify_token(token):
    token_prefix = read(APPLICATION_CONFIG, 'jwt.token_prefix')
    return verify_tk('%s%s' % (token_prefix, token))


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
                 fields=e.fields if hasattr(e, 'fields') else None, http_status=400)


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
    return error(description='Internal Server Error.', http_status=constant.INTERNAL_ERROR)


@app.errorhandler(Exception)
def error_handler(e):
    logger.error(traceback.format_exc())
    return error(status=constant.INTERNAL_ERROR, description='Internal Server Error.',
                 http_status=constant.INTERNAL_ERROR)
