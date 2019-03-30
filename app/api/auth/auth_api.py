from flask import request
from app.service.UserService import user_service
from app.util.Resp import success
from app.util import JwtUtils
from app.api import basic_auth
from . import auth_bp as api


@api.route('/token', methods=['POST'])
@basic_auth.login_required
def token():
    username_auth = request.authorization.get('username') if request.authorization else None
    user = user_service.find_by_username(username_auth or request.json['username'])
    return success(data=JwtUtils.encode_auth_token(user.id, user.username))


@api.route('/logout', methods=['POST'])
def logout():
    return success()

