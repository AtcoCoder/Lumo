from flask import Flask
from config import DevelopmentConfig
from models import db
from models.blocked_token import BlockedToken
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bootstrap import Bootstrap5


def create_app(config_object=DevelopmentConfig):
    """Factory to create and config flask app instance"""
    app = Flask(__name__)
    app.config.from_object(config_object)

    return app


app = create_app()
migrate = Migrate(app, db)
bootstrap = Bootstrap5(app)


from home import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
