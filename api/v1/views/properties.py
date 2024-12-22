"""Property views module"""
from models.property import Property
from api.v1.views import app_views
from flask import jsonify, request


@app_views.route('/properties', strict_slashes=False)
def get_properties():
    all_properties = Property.get_all()
    return jsonify(properties=all_properties)
