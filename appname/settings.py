class Config(object):
    pass


class DevConfig(Config):
    ENV = 'dev'
    # DEBUG = True


class ProdConfig(Config):
    ENV = 'prod'


class TestConfig(Config):
    ENV = 'test'
    # DEBUG = True
