# -*- coding: utf-8 -*-
from flask import Blueprint
from app.api import context_path

auth_bp = Blueprint('auth', __name__, url_prefix='%s/auth' % context_path)

# 解决循环应用问题，请勿移至顶部
from app.api.auth import authentication_api
