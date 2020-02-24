import logging
import logging.handlers
from flask import Flask, jsonify
from voluptuous.error import Invalid

from app.router import main
from config import config


def create_app(environment: str = None):
    """
    Arguments:
        environment: str environment type
    """

    app = Flask(__name__)
    environment_config = config(environment)
    # set config
    app.config.from_object(environment_config)

    #  自定义路由前缀
    #  app.register_blueprint(main, url_prefix='/api/v1')
    app.register_blueprint(main)

    # logger config
    app.logger.setLevel(logging.DEBUG)
    app.logger.handlers.extend(logging.getLogger("flask.base").handlers)
    app.logger.handlers.extend(logging.getLogger("flask.error").handlers)

    @app.errorhandler(500)
    def internal_server_error(e):
        app.log_exception(e)
        if isinstance(e, Invalid):
            return jsonify({"code": 44013, "data": "Params Error"}), 500
        else:
            return jsonify({"code": 500, "data": "Something Error"}), 500

    return app
