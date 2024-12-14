"""__init__"""
from flask import Flask
from config import DevelopmentConfig
from api.v1.views import app_views


def create_app(config_object=DevelopmentConfig):
    """Factory to create and config flask app instance"""
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(app_views)

    return app
