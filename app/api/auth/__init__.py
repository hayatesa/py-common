from flask import Blueprint
from app.api import context_path

auth_bp = Blueprint('auth', __name__, url_prefix='%s/auth' % context_path)

from . import auth_api
