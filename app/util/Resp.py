from app.util.JsonUtils import to_json
from datetime import datetime
from flask import Response

MIME_TYPE = 'application/json;charset=utf-8'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DEFAULT_MESSAGE = ''


class Resp:

    def __init__(self, success=True, message=DEFAULT_MESSAGE, data=None):
        self.success = success
        self.message = message
        self.timestamp = datetime.now().strftime(DATETIME_FORMAT)
        self.data = data

    def to_json(self):
        return to_json(self)


def mk_resp(success=True, message=DEFAULT_MESSAGE, data=None, status_code=200):
    resp = Response(Resp(success, message, data).to_json(), mimetype=MIME_TYPE)
    resp.status_code = status_code
    return resp


def success(message=DEFAULT_MESSAGE, data=None):
    resp = Response(Resp(True, message, data).to_json(), mimetype=MIME_TYPE)
    return resp


def failure(message=DEFAULT_MESSAGE, data=None, status_code=200):
    resp = Response(Resp(False, message, data).to_json(), mimetype=MIME_TYPE)
    resp.status_code = status_code
    return resp
