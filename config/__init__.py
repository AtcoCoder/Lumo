"""Init module"""
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()


class Config(object):
    """Base config"""
    TESTING = False


class ProductionConfig(Config):
    """Production configurations"""
    DATABASE_URL = os.getenv('DATABASE_URL')        
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')


class DevelopmentConfig(Config):
    """Development configurations"""
    DATABASE_URI = 'mysql+mysqlconnector://atcocoder:password@localhost/Lumo'
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS  = False
    DEBUG = True
    SECRET_KEY = 'dev'
    JWT_SECRET_KEY = 'secret_key'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=30)

class TestingConfig(Config):
    """Testing Configurations"""
    DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
    JWT_SECRET_KEY = 'secret_key'


CURRENT_CONFIG = ProductionConfig
