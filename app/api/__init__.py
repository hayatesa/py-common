from app import app, APPLICATION_CONFIG
from app.util.Resp import failure

from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask import request, abort
from werkzeug.security import check_password_hash

from app.exception.AuthException import AuthException
from app.exception.TokenException import TokenException
from app.exception.LoginException import LoginException
from app.service.UserService import user_service
import datetime

from app.util import JwtUtils

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
        raise LoginException(message='请提供用户名')
    if not _password:
        raise LoginException(message='请提供密码')

    user_info = user_service.find_by_username(_username)
    if not user_info:
        raise LoginException(message='用户不存在')
    if not check_password_hash(user_info.password, _password):
        raise LoginException(message='密码错误')
    user_info.lastAccessTime = datetime.datetime.now()
    user_service.update(user_info)
    return True


@token_auth.verify_token
def verify_token(token):
    if not token:
        abort(401, **{'description': '令牌缺失'})

    payload = JwtUtils.decode_auth_token(token)
    if not JwtUtils.is_valid_token(payload):
        raise TokenException('令牌无效')
    if JwtUtils.is_token_expired(payload['exp']):
        abort(401, **{'description': '令牌过期'})
    return True


# 全局异常处理
@app.errorhandler(400)
def bad_request(error):
    return failure(message=error.description, status_code=error.code)


@app.errorhandler(401)
def unauthorized(error):
    return failure(message=error.description, status_code=error.code)


@app.errorhandler(403)
def forbidden(error):
    return failure(message=error.description, status_code=error.code)


@app.errorhandler(404)
def not_found(error):
    return failure(message=error.description, status_code=error.code)


@app.errorhandler(405)
def method_not_allowed(error):
    return failure(message=error.description, status_code=error.code)


@app.errorhandler(500)
def internal_server_error(error):
    return failure(message=error.description, status_code=error.code)


@app.errorhandler(AuthException)
def auth_exception(e):
    return failure(message=e.message)


@app.errorhandler(TokenException)
def token_exception(e):
    return failure(message=e.message, status_code=401)


@app.errorhandler(LoginException)
def login_exception(e):
    return failure(message=e.message)


@app.errorhandler(Exception)
def exception():
    return failure(message='Internal Error.', status_code=500)
