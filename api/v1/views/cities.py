"""City views module"""
from models.city import City
from models.area import Area
from api.v1.views import app_views
from flask import jsonify, request


@app_views.route('/cities', strict_slashes=False)
def get_cities():
    """Get all cities route"""
    all_cities = City.get_all()
    return jsonify(cities=all_cities)


@app_views.route(
    '/cities/add',
    methods=['POST'],
    strict_slashes=False
)
def add_city():
    """Add city route"""
    name = request.form.get('name')
    area_name = request.form.get('area_name')
    area = Area.get_by_name(area_name)
    if not area:
        return jsonify(message='Area Not Found')
    city = City(
        name=name,
        area_id=area.id
    )
    city.save()
    return jsonify(message='City successfully created')


@app_views.route(
    '/cities/<city_id>',
    strict_slashes=False
)
def get_city(city_id):
    """Get city route"""
    city = City.get(city_id)
    if not city:
        return jsonify(message='City Not Found')
    return jsonify(city=city.to_dict_with('properties', city.properties))


@app_views.route(
    '/cities/<city_id>',
    strict_slashes=False,
    methods=['PATCH', 'DELETE']
)
def w_city(city_id):
    """Update/Delete city route"""
    city = City.get(city_id)
    if not city:
        return jsonify(message='City Not Found')
    if request.method == 'PATCH':
        name = request.form.get('name')
        if not name:
            return jsonify(message='Missing name')
        city.name = name
        city.save()
        return jsonify(message='City Name successfully changed')
    city.delete()
    return jsonify(message='Successfully deleted')
