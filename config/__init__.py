"""Init module"""


class Config(object):
    """Base config"""
    TESTING = False


class ProductionConfig(Config):
    """Production configurations"""
    DATABASE_URI = ''
    SECRET_KEY = ''


class DevelopmentConfig(Config):
    """Development configurations"""
    DATABASE_URI = ''
    DEBUG = True
    SECRET_KEY = 'dev'


class TestignConfig(Config):
    """Testing Configurations"""
    DATABASE_URI = ''
    TESTING = True
