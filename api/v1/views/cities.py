"""City views module"""
from models.city import City
from models.area import Area
from api.v1.views import app_views
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt


@app_views.route('/cities', strict_slashes=False)
def get_cities():
    """Get all cities route"""
    all_cities = City.get_all()
    return jsonify(cities=all_cities)


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
    '/cities/<city_id>/properties',
    strict_slashes=False
)
def get_city_properties(city_id):
    """Get city properties route"""
    city = City.get(city_id)
    if not city:
        return jsonify(message='City Not Found.'), 400
    properties = city.properties
    property_list = []
    for property in properties:
        property_dict = property.to_dict_with('amenities', property.amenities)
        property_dict['images'] = property.its('images')
        property_list.append(property_dict)
    return jsonify(properties=property_list)


####################################################################################
####                            Admin regions Routes                            ####
####################################################################################


@app_views.route(
    '/admin/cities/<city_id>',
    strict_slashes=False,
    methods=['PATCH', 'DELETE']
)
@jwt_required()
def w_city(city_id):
    """Update/Delete city by admin"""
    claims = get_jwt()
    role = claims.get('role')
    if role != 'Admin':
        return jsonify(msg="Access forbidden"), 403
    city = City.get(city_id)
    if not city:
        return jsonify(message='City Not Found')
    if request.method == 'PATCH':
        data = request.get_json()
        name = data.get('name')
        if not name:
            return jsonify(message='Missing name')
        city.name = name
        city.save()
        return jsonify(message='City Name successfully changed')
    city.delete()
    return jsonify(message='Successfully deleted')
