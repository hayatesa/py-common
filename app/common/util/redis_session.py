# -*- coding: utf-8 -*-
from app.auth import APPLICATION_CONFIG
from app.common.util.redis_util import client

PREFIX = APPLICATION_CONFIG['session'].get('key_prefix', '')
EXPIRE = APPLICATION_CONFIG['session'].get('expire', 1800)


class Session:

    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def get_key(self):
        return PREFIX + self.key

    def create(self):
        client.setex(self.get_key(), EXPIRE, self.value)
        return self

    def read(self):
        return client.get(self.get_key())

    def update(self, value):
        client.setex(self.get_key(), EXPIRE, value)
        return self

    def delete(self):
        client.delete(self.get_key())
        return self
