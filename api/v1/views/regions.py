"""Region views module"""
from models.region import Region
from models.area import Area
from api.v1.views import app_views
from flask import jsonify, request
from flask_jwt_extended import jwt_required

@app_views.route('/regions/add', methods=['POST'], strict_slashes=False)
def add_region():
    """Add region route"""
    name = request.form.get('name')
    region = Region.get_by_name(name)
    if region:
        return jsonify(message='Region already exist')
    region = Region(
        name=name
    )
    region.save()
    return jsonify(message='Region successfully added')

@app_views.route('/regions')
def get_regions():
    """Get all regions route"""
    regions = Region.get_all()
    return jsonify(regions=regions)


@app_views.route('/regions/<region_id>', strict_slashes=False)
def get_region(region_id):
    """Get region route"""
    region = Region.get(region_id)
    if not region:
        return jsonify(message="Region Not Found"), 400
    region_dict = region.to_dict_with('areas', region.areas)
    return jsonify(region=region_dict)


@app_views.route(
    '/regions/<region_id>',
    methods=['DELETE', 'PATCH'],
    strict_slashes=False
)
def w_regions(region_id):
    """Delete/Update region route"""
    region = Region.get(region_id)
    if not region:
        return jsonify(message="Region Not Found"), 400
    if request.method == 'DELETE':
        region.delete()
        return jsonify(message='Successfully deleted')
    to_update = ['name']
    to_updates = region.get_infos_to_update(request, to_update)
    region.update(**to_updates)
    return jsonify(message='Succesfully updated')


@app_views.route(
    '/regions/<region_id>/add_area',
    methods=['POST'],
    strict_slashes=False
)
def add_area_to_region(region_id):
    """Add area to a region"""
    region = Region.get(region_id)
    if not region:
        return jsonify(message='Region Not Found'), 400
    name = request.form.get('name')
    area = Area(
        name=name,
        region_id=region_id
    )
    return jsonify(message='Successfully added')

@app_views.route(
    '/regions/<region_id>/areas',
    strict_slashes=False
)
def get_region_areas(region_id):
    """Get region areas route"""
    region = Region.get(region_id)
    if not region:
        return jsonify(message='Region Not Found'), 400
    areas = region.its('areas', 'cities')
    return jsonify(areas=areas)
