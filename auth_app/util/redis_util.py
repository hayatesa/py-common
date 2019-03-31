import redis

from auth_app.exception import InternalException


class RedisUtil:
    """
    See:
    http://www.cnblogs.com/melonjiang/p/5342383.html
    http://www.cnblogs.com/melonjiang/p/5342505.html
    """

    def __init__(self):
        pool = redis.ConnectionPool(host='119.29.94.246', port=6379, decode_responses=True,
                                    password='redis272243')
        self.client = redis.Redis(connection_pool=pool)

    def get_redis(self):
        return self.client

    def publish(self, channel, message):
        if not channel:
            raise InternalException(message='channel should not be None')
        if not channel:
            raise InternalException(message='message should not be None')
        self.client.publish(channel, message)

    def subscribe(self, channel):
        pub = self.client.pubsub()
        pub.subscribe(channel)
        pub.parse_response()
        return pub


redis_util = RedisUtil()
del RedisUtil
