def read(dict_obj=None, key=None, default=None, splitter='.'):
    """根据 key 获取 dict 中的 value

    :param dict_obj: dict对象
    :param key: 使用分隔符连接的key字符串，如'log.handlers.console.level'
    :param default: 默认值
    :param splitter: key分隔符，默认为'.'
    :return: 如果值存在，返回该值，否则返回default值
    """
    k = key.strip()
    if not k or not isinstance(dict_obj, dict):
        return default
    segments = k.split(splitter)
    if not segments:
        return default

    # 递归访问dict
    def visit(_dict_obj, _segments):
        if not isinstance(_dict_obj, dict):
            return None
        if len(_segments) == 1:
            return _dict_obj.get(_segments[0])
        return visit(_dict_obj.get(_segments[0]), _segments[1:])

    result = visit(dict_obj, segments)
    return default if isinstance(result, type(None)) else result


if __name__ == '__main__':
    print(read({'jwt': {'prefix': {'p1': 'session.'}}}, 'jwt.prefix.p1'))
