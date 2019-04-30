# -*- coding: utf-8 -*-
from flasgger import Swagger
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import sys
import time
import logging.config
from yaml import safe_load

start_time = time.time()

CONTEXT_PATH = sys.path[0]  # 应用上下文路径

RESOURCES_PATH = CONTEXT_PATH  # 资源文件路径

CONF_FILE_INFO = {'filename': 'application', 'suffix': '.yml'}
CONFIG_FILE_PATH = os.path.join(RESOURCES_PATH, '%s%s' % (CONF_FILE_INFO['filename'],
                                                          CONF_FILE_INFO['suffix']))  # 应用配置文件路径

BANNER_PATH = os.path.join(RESOURCES_PATH, 'banner.txt')  # banner路径


def read_dict(dict_obj=None, key=None, default=None, splitter='.'):
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


def _load_config():
    """加载系统配置 即application[-profile].yml"""
    app_config = {}
    _logger = logging.getLogger()
    _logger.setLevel(logging.DEBUG)
    if os.path.exists(CONFIG_FILE_PATH):
        try:
            with open(CONFIG_FILE_PATH, encoding='UTF-8') as f:
                conf = safe_load(f)
                app_config = dict(app_config, **conf) if conf else app_config
        except Exception as e:
            _logger.error(e)
            sys.exit(1)
    else:
        _logger.error('无法找到文件%s' % CONFIG_FILE_PATH)
        sys.exit(1)

    profile = app_config.get('profile')
    # 如果指定了profile, 加载profile配置文件
    if profile:
        profile_path = os.path.join(RESOURCES_PATH, '%s-%s%s' % (CONF_FILE_INFO['filename'],
                                                                 profile,
                                                                 CONF_FILE_INFO['suffix']))
        if os.path.exists(profile_path):
            try:
                with open(profile_path, encoding='UTF-8') as f:
                    conf = safe_load(f)
                    app_config = dict(app_config, **conf) if conf else app_config
            except Exception as e:
                _logger.error(e)
                sys.exit(1)
        else:
            _logger.warning('无法找到文件%s, 请检查profile拼写是否有误' % profile_path)

    return app_config


def _create_logger():
    """创建logger"""
    log_conf = APPLICATION_CONFIG.get('log')
    if not log_conf:
        return logging.getLogger()
    log_conf['version'] = log_conf.get('version', 1)
    logging.config.dictConfig(log_conf)
    _app_logger = logging.getLogger('app')
    return _app_logger


def _create_swagger(flask_app):
    """创建swagger文档"""
    swagger_config = APPLICATION_CONFIG.get('swagger')
    if not swagger_config:
        return None
    return Swagger(flask_app, config=swagger_config)


def _create_db(flask_app):
    _db = SQLAlchemy()
    _db.init_app(flask_app)
    return _db


def _create_app__():
    flask_app = Flask(__name__, static_folder=os.path.join(
        CONTEXT_PATH,
        read_dict(APPLICATION_CONFIG, 'server.static_folder', 'templates')
    ))
    flask_app.config.from_mapping(APPLICATION_CONFIG.get('sqlalchemy', {}))
    _init_cors(flask_app)
    return flask_app


def _init_cors(flask_app):
    cors = read_dict(APPLICATION_CONFIG, 'server.cors')
    supports_credentials = cors.get('allow') is True
    origins = (cors.get('origins') if cors.get('origins') else '*') if supports_credentials else ''
    path = (cors.get('path') if cors.get('path') else '/*') if supports_credentials else ''
    CORS(flask_app, supports_credentials=supports_credentials,
         resources={path: {"origins": origins}})


def _assemble_blueprint(flask_app):
    from app.auth.api.auth import auth_bp
    flask_app.register_blueprint(auth_bp)


def _message():
    """打印启动信息"""
    if os.path.exists(BANNER_PATH):
        logger.info('Load banner.txt from %s' % BANNER_PATH)
        with open(BANNER_PATH, encoding='UTF-8') as f:
            logger.info(f.read())
    logger.info('Application launched in %.2f Seconds.' % (end_time - start_time))


APPLICATION_CONFIG = _load_config()
logger = _create_logger()
app = _create_app__()
swagger = _create_swagger(app)
db = _create_db(app)
_assemble_blueprint(app)

end_time = time.time()
_message()
