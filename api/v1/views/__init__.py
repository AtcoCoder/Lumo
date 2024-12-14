"""api/v1/views/__init__"""
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.regions import *
from api.v1.views.areas import *
from api.v1.views.cities import *
from api.v1.views.images import *
from api.v1.views.properties import *
