"""Region views module"""
from models.region import Region
from api.v1.views import app_views
from flask import jsonify, request
from flask_jwt_extended import jwt_required

@app_views.route('/regions/add', methods=['POST'], strict_slashes=False)
def add_region():
    """Add region route"""
    name = request.form.get('name')
    region = Region(
        name=name
    )
    return jsonify(message='Region successfully added')
