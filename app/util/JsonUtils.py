import datetime
import json

from sqlalchemy.ext.declarative import DeclarativeMeta

DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
EXCLUDE_FIELDS = ['metadata', 'query', 'query_class']
EXCLUDE_ALCHEMY_FIELDS = []


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):

        exclude = EXCLUDE_FIELDS  # exclude fields
        if isinstance(obj.__class__, DeclarativeMeta):
            exclude.append(EXCLUDE_ALCHEMY_FIELDS)
        dict_obj = {}
        for field in [x for x in dir(obj) if not x.startswith('_') and x not in exclude]:
            data = obj.__getattribute__(field)
            if callable(data):
                continue
            try:
                json.dumps(data, ensure_ascii=False)  # this will fail on non-encodable values, like other classes
                dict_obj[field] = data
            except TypeError:  # 添加了对datetime的处理
                if isinstance(data, datetime.datetime):
                    # fields[field] = data.isoformat()
                    dict_obj[field] = data.strftime(DATE_TIME_FORMAT)
                elif isinstance(data, datetime.date):
                    dict_obj[field] = data.isoformat()
                elif isinstance(data, datetime.timedelta):
                    dict_obj[field] = (datetime.datetime.min + data).time().isoformat()
                else:
                    dict_obj[field] = None
        # a json-encodable dict
        return dict_obj


def to_json(obj):
    return json.dumps(obj.__dict__, cls=AlchemyEncoder, ensure_ascii=False)
