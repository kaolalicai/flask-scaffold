import os
from config import config as config_, logConfig

conf = config_()
loglevel = conf.app_log_level
workers = conf.gunicorn_workers
threads = conf.gunicorn_threads
timeout = conf.gunicorn_timeout
worker_class = conf.gunicorn_worker_class
bind = conf.app_base_url
logconfig_dict = logConfig
project_path = conf.project_path


def on_starting(server):
    if 'log' not in os.listdir(project_path):
        os.mkdir(project_path + '/log')

