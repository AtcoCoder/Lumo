"""app module"""
from flask import Flask
from config import DevelopmentConfig
from models.base_model import Base
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


def create_app(config_object=DevelopmentConfig):
    """Factory to create and config flask app instance"""
    app = Flask(__name__)
    app.config.from_object(config_object)
    from api.v1.views import app_views
    app.register_blueprint(app_views)



    return app


app = create_app()
migrate = Migrate(app, Base)
jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
