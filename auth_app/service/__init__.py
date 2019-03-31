# -*- coding: utf-8 -*-
from sqlalchemy.exc import SQLAlchemyError
from auth_app import db


def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e
