# -*- coding: utf8 -*-

from flask import Flask, render_template, jsonify
from web_server.factory import psql, redis
from web_server.utility.api_exception import ApiException


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        return render_template('index.html')

    setup_db(app)
    setup_cache(app)
    setup_blueprints(app)

    @app.errorhandler(ApiException)
    def handler_api_exception(error):
        response = dict(status=error.status, message=error.message)
        return str(response)

    return app


def setup_db(app):
    psql.app = app
    psql.init_app(app)


def setup_cache(app):
    redis.init_app(app)


def setup_blueprints(app):
    from web_server.view.main import blueprint as main

    blueprints = [
        {'handler': main, 'url_prefix': '/main'}
    ]

    for bp in blueprints:
        app.register_blueprint(bp['handler'], url_prefix=bp['url_prefix'])
