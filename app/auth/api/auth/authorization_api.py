# -*- coding: utf-8 -*-

from app.auth.api.auth import auth_bp as api


@api.route('/role/<role>')
def verify_role(role):
    pass


@api.route('/permission/<permission>')
def verify_permission(permission):
    pass
