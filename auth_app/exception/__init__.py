# -*- coding: utf-8 -*-
"""全局异常定义"""


class AuthenticationException(Exception):

    def __init__(self, message=''):
        self.message = message


class AuthorizationError(Exception):

    def __init__(self, message=''):
        self.message = message


class BusinessException(Exception):

    def __init__(self, message='', status=None):
        self.message = message
        self.status = status


class InternalException(Exception):

    def __init__(self, message=''):
        self.message = message
