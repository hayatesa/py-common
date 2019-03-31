# -*- coding: utf-8 -*-
class UserVo:

    def __init__(self, user_id, username, name, avatar, last_access_time):
        self.id = user_id
        self.username = username
        self.name = name
        self.avatar = avatar
        self.lastAccessTime = last_access_time

    @staticmethod
    def convert(source):
        return UserVo(source.id, source.username, source.name, source.avatar, source.lastAccessTime)
