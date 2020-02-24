"""develop(default) config"""
import os


class BaseConfig(object):
    environment = 'default'

    # app config
    app_name = 'flask-docker-scaffold'
    app_base_url = '0.0.0.0:5000'
    app_log_level = 'debug'

    # project config
    project_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

    # gunicorn config
    gunicorn_workers = '2'
    gunicorn_threads = '1'
    gunicorn_timeout = '180'
    gunicorn_worker_class = 'gevent'

