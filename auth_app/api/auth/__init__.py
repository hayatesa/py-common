# -*- coding: utf-8 -*-
from flask import Blueprint
from auth_app.api import context_path

auth_bp = Blueprint('auth', __name__, url_prefix='%s/auth' % context_path)

from auth_app.api.auth import auth_api  # 解决循环应用问题，请勿移至顶部
