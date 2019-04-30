import redis

from app.common.exception import InternalError
from app.auth import APPLICATION_CONFIG


class RedisUtil:
    """
    See:
    http://www.cnblogs.com/melonjiang/p/5342383.html
    http://www.cnblogs.com/melonjiang/p/5342505.html
    """

    def __init__(self):
        redis_config = APPLICATION_CONFIG.get('redis')
        if not redis_config:
            return
        if not redis_config.get('active'):
            return
        if not redis_config:
            raise InternalError(description="未找到redis配置")
        host = redis_config.get('host')
        if not host:
            raise InternalError(description="未找到redis.host配置")
        port = redis_config.get('port', 6379)
        if not host:
            raise InternalError(description="未找到redis.port配置")
        password = redis_config.get('password')
        if not password:
            raise InternalError(description="未找到redis.password配置")
        decode_responses = redis_config.get('decode_responses', False)
        pool = redis.ConnectionPool(host=host, port=port, decode_responses=decode_responses, password=password)
        self.client = redis.Redis(connection_pool=pool)

    def get_redis(self):
        return self.client if hasattr(self, 'client') else None

    def publish(self, channel, description):
        if not channel:
            raise InternalError(description='channel should not be None')
        if not channel:
            raise InternalError(description='description should not be None')
        self.client.publish(channel, description)

    def subscribe(self, channel):
        pub = self.client.pubsub()
        pub.subscribe(channel)
        pub.parse_response()
        return pub


redis_util = RedisUtil()
client = redis_util.get_redis()
del RedisUtil
