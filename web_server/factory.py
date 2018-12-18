# -*- coding: utf8 -*-

from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

__all__ = ['psql', 'redis']


class RedisClient(StrictRedis):
    def __init__(self, app=None):
        super().__init__()
        self.app = app
        if app is not None:  # pragma: no cover
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        host, port = 'localhost', 6379
        db = 0
        super().__init__(host=host, port=port, db=db, decode_responses=True)


# sql database
psql = SQLAlchemy()
psql.slave_session = psql.session

# redis cache
redis = RedisClient()
