"""Init module"""


class Config(object):
    """Base config"""
    TESTING = False


class ProductionConfig(Config):
    """Production configurations"""
    DATABASE_URI = ''
    SECRET_KEY = ''
    JWT_SECRET_KEY = ''


class DevelopmentConfig(Config):
    """Development configurations"""
    DATABASE_URI = 'mysql+mysqlconnector://atcocoder0:password@localhost/Lumo'
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS  = False
    DEBUG = True
    SECRET_KEY = 'dev'
    JWT_SECRET_KEY = 'secret_key'

class TestingConfig(Config):
    """Testing Configurations"""
    DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
    JWT_SECRET_KEY = 'secret_key'


CURRENT_CONFIG = DevelopmentConfig
