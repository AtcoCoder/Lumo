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
    DATABASE_URI = 'sqlite:///lumo.db'
    DEBUG = True
    SECRET_KEY = 'dev'


class TestingConfig(Config):
    """Testing Configurations"""
    DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True


CURRENT_CONFIG = DevelopmentConfig
