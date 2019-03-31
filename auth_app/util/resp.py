from auth_app.util.json_util import to_json
from flask import Response
import auth_app.constant as constant

MIME_TYPE = 'application/json;charset=utf-8'
DEFAULT_MESSAGE = ''


class Resp:

    def __init__(self, status=0, message=DEFAULT_MESSAGE, data=None):
        self.status = status
        self.message = message
        self.data = data

    def to_json(self):
        return to_json(self)


def mk_resp(status=constant.SUCCESS_STATUS, message=DEFAULT_MESSAGE, data=None, http_status_code=200):
    resp = Response(Resp(status, message, data).to_json(), mimetype=MIME_TYPE)
    resp.status_code = http_status_code
    return resp


def success(message=DEFAULT_MESSAGE, data=None):
    resp = Response(Resp(constant.SUCCESS_STATUS, message, data).to_json(), mimetype=MIME_TYPE)
    return resp


def failure(status=constant.FAILURE_STATUS, message=DEFAULT_MESSAGE, data=None, http_status_code=200):
    resp = Response(Resp(status, message, data).to_json(), mimetype=MIME_TYPE)
    resp.status_code = http_status_code
    return resp
