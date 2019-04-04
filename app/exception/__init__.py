# -*- coding: utf-8 -*-
"""全局异常定义"""


class AuthenticationError(Exception):

    def __init__(self, description=None):
        if description:
            self.description = description


class AuthorizationError(Exception):

    def __init__(self, description=None):
        if description:
            self.description = description


class BusinessError(Exception):

    def __init__(self, description=None):
        if description:
            self.description = description


class ParameterError(Exception):

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


class UnprocessableParameterError(Exception):
    """无效参数错误，通常在参数校验不通过是抛出"""

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


class ResourceNotFoundError(Exception):
    def __init__(self, description=None):
        if description:
            self.description = description


class ResourceConflictError(Exception):
    def __init__(self, description=None):
        if description:
            self.description = description


class InternalError(Exception):

    def __init__(self, description=None):
        self.description = description
