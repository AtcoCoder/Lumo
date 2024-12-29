"""Amenity view module"""
from models.amenity import Amenity
from flask import request, jsonify
from api.v1.views import app_views


@app_views.route('/amenities/add', methods=['POST'], strict_slashes=False)
def add_amenities():
    """Add amenities route"""
    name = request.form.get('name')
    if not name:
        return jsonify(message='Missing name'), 400
    amenity = Amenity.get_by_name(name)
    if amenity:
        return jsonify(message='Amenity alread exist'), 400
    
    amenity = Amenity(
        name=name,
        amount=1
    )
    amenity.save()
    return jsonify(message='Amenity successfully added.')


@app_views.route('/amenities', strict_slashes=False)
def get_amenities():
    amenities = Amenity.get_all()
    return jsonify(amenities=amenities)

@app_views.route(
    '/amenity/<amenity_id>',
    methods=['DELETE', 'PATCH'],
    strict_slashes=False
)
def w_amenities(amenity_id):
    """Delete/Update amenity route"""
    amenity = Amenity.get(amenity_id)
    if not amenity:
        return jsonify(message="Amenity Not Found"), 400
    if request.method == 'DELETE':
        amenity.delete()
        return jsonify(message='Successfully deleted')
    to_update = ['name']
    to_updates = amenity.get_infos_to_update(request, to_update)
    amenity.update(**to_updates)
    return jsonify(message='Succesfully updated')

