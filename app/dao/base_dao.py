# -*- coding: utf-8 -*-
from app import db


class BaseDAO:

    def __init__(self, mapper):
        self.__mapper = mapper

    def list(self):
        mapper = self.__mapper
        return mapper.query.filter(mapper.isDeleted == False).all()

    def find(self, id):
        mapper = self.__mapper
        return mapper.query.filter(mapper.isDeleted == False, mapper.id == id).all()

    def delete(self, id):
        db.session.delete(self.find(id))

    def add(self, obj):
        db.session.add(obj)

    def update(self, obj):
        db.session.add(obj)
