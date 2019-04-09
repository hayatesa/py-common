# -*- coding: utf-8 -*-
"""全局异常定义"""
from app import constant


class BaseError(Exception):
    """所有异常的父类"""

    def __init__(self, description):
        self.description = description


class DAOError(BaseError):
    """数据库异常"""

    def __init__(self, description):
        super(DAOError, self).__init__(description)


class ServiceError(BaseError):
    """业务逻辑异常"""

    def __init__(self, description, status=constant.SERVICE_ERROR):
        super(ServiceError, self).__init__(description)
        self.status = status


class InternalError(BaseError):
    """内部异常"""

    def __init__(self, description):
        super(InternalError, self).__init__(description)


class AuthenticationError(ServiceError):
    """认证异常"""

    def __init__(self, description=None):
        self.status = constant.INVALID_TOKEN
        if description:
            self.description = description


class AuthorizationError(ServiceError):
    """权限异常"""

    def __init__(self, description=None):
        self.status = constant.FORBIDDEN
        if description:
            self.description = description


class ParameterInvalidError(ServiceError):
    """参数异常"""

    def __init__(self, description=None, **fields):
        self.status = constant.BAD_REQUEST
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
        self.fields = self.fields if hasattr(self, 'fields') else {}
        self.fields = dict(self.fields, **fields)
        return self
