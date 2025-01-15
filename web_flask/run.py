from flask import Flask
from models import db
from models.blocked_token import BlockedToken
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bootstrap import Bootstrap5
from config import CURRENT_CONFIG



def create_app(config_object=CURRENT_CONFIG):
    """Factory to create and config flask app instance"""
    app = Flask(__name__)
    app.config.from_object(config_object)

    return app


app = create_app()
migrate = Migrate(app, db)
bootstrap = Bootstrap5(app)


from home import *

if __name__ == '__main__':
    app.run(threaded=True)
