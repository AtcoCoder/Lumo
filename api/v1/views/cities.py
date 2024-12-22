"""City views module"""
from models.city import City
from api.v1.views import app_views
from flask import jsonify, request


@app_views.route('/cities')
def get_cities():
    """Get all cities route"""
    all_cities = City.get_all()
    return jsonify(cities=all_cities)


@app_views.route('/city/add')
def add_city():
    """Add city route"""
    name = request.form.get('name')
    city = City(
        name=name
    )
