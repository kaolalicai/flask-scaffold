import logging
import logging.handlers
from flask import Flask, jsonify

from config import config
from app.router import main


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
    app.register_blueprint(main)
    #  app.register_blueprint(main, url_prefix='/api/v1')

    # logger config
    app.logger.setLevel(logging.DEBUG)
    app.logger.handlers.extend(logging.getLogger("flask.base").handlers)
    app.logger.handlers.extend(logging.getLogger("flask.error").handlers)

    # 在这里可以配置相应的错误号码, 或者指定的Exception
    @app.errorhandler(500)
    def internal_server_error(e):
        app.log_exception(e)
        return jsonify({"code": 500, "data": "Server Error"}), 500

    return app
