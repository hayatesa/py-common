from app.util.json_util import to_json
from flask import Response
import app.constant as constant

MIME_TYPE = 'application/json;charset=utf-8'
DEFAULT_MESSAGE = ''


class Resp:

    def __init__(self):
        pass

    @classmethod
    def success(cls, message=constant.SUCCESS_MESSAGE, data=None):
        """请求成功结果

        :param message: 消息
        :param data: 数据
        """
        resp = cls()
        resp.message = message
        resp.data = data
        return resp

    @classmethod
    def error(cls, status=constant.INTERNAL_ERROR, description=None, fields=None):
        """请求失败结果

        :param status: 错误状态码
        :param description: 用户可读的错误消息
        :param fields: 字段描述，通常用于描述请求参数的错误
        """
        resp = cls()
        _error = cls()
        _error.status = status
        if description:
            _error.description = description
        if fields:
            _error.fields = fields
        resp.error = _error
        return resp

    def to_json(self):
        return to_json(self)


def success(message=constant.SUCCESS_MESSAGE, data=None):
    """请求成功结果

    :param message: 消息
    :param data: 数据
    """
    return Response(Resp.success(message=message, data=data).to_json(), mimetype=MIME_TYPE)


def error(status=None, description=None, fields=None,
          http_status=constant.INTERNAL_ERROR):
    """请求失败结果

    :param status: 错误状态码
    :param description: 用户可读的错误消息
    :param fields: 字段描述，通常用于描述请求参数的错误
    :param http_status: http状态码
    """
    resp = Response(Resp.error(status=status, description=description, fields=fields).to_json(), mimetype=MIME_TYPE)
    resp.status_code = http_status
    return resp
