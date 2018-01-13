import os
import logging
import logging.handlers
from flask import Flask, jsonify
from voluptuous.error import Invalid

from .controllers.main import main


def create_app(object_name):
    """
    Arguments:
        object_name: the python path of config object,
                     e.g. appname.settings.ProduConfig
    """

    app = Flask(__name__)

    app.config.from_object(object_name)

    #  自定义路由前缀
    #  app.register_blueprint(main, url_prefix='/api/v1')
    app.register_blueprint(main)

    # 输出loglog
    log_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]+'/logs'
    log_name = '/logs.log'
    handler = logging.handlers.WatchedFileHandler(
        log_path+log_name
    )
    fo = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(fo)
    app.logger.addHandler(handler)

    @app.errorhandler(500)
    def internal_server_error(e):
        app.log_exception(e)
        if isinstance(e, Invalid):
            return jsonify({"code": 44013, "data": "参数格式错误"}), 500
        else:
            return jsonify({"code": 500, "data": "服务器出小差"}), 500

    return app
