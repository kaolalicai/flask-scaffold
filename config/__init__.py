import os
from config.base import BaseConfig
from config.develop import DevConfig
from config.production import ProdConfig
from config.test import TestConfig
from config.log import logConfig

config_dict = {
    'develop': DevConfig,
    'production': ProdConfig,
    'test': TestConfig,
    'default': BaseConfig
}


def config(environment: str = None):
    environment = environment or os.environ.get('ENVIRONMENT', 'default')
    return config_dict[environment]
