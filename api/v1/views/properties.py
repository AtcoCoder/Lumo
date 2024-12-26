"""Property views module"""
from models.property import Property
from api.v1.views import app_views
from flask import jsonify, request


@app_views.route('/properties', strict_slashes=False)
def get_properties():
    all_properties = Property.get_all()
    # import pprint
    # pprint.pprint(all_properties)
    return jsonify(properties=all_properties)


@app_views.route(
    '/properties/<property_id>',
    strict_slashes=False
)
def get_property_by(property_id):
    """Get property route"""
    property = Property.get(property_id)
    if not property:
        return jsonify(message='Property not found'), 400
    
    property_dict = property.to_dict()
    property_dict['images'] = property.its('images')
    property_dict['amenities'] = property.its('amenities')
    return jsonify(property=property_dict)
