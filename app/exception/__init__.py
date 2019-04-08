# -*- coding: utf-8 -*-
"""全局异常定义"""


class BaseError(Exception):

    def __init__(self):
        pass


class AuthenticationError(BaseError):

    def __init__(self, description=None):
        if description:
            self.description = description


class AuthorizationError(BaseError):

    def __init__(self, description=None):
        if description:
            self.description = description


class ParameterError(BaseError):

    def __init__(self, description=None, fields=None):
        if description:
            self.description = description
        if fields:
            self.fields = fields

    def put_fields(self, **fields):
        """添加描述字段

        :param fields: 如
          {'username': 'Field username should not be blank.', 'password': 'Length of password should be longer than 8.'}
        :return: self
        """
        dict(self.fields, **fields)
        return self


class BusinessError(BaseError):

    def __init__(self, description=None):
        if description:
            self.description = description


class ServiceError(BaseError):

    def __init__(self, description=None):
        self.description = description
