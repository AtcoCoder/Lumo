"""Region views module"""
from models.region import Region
from models.area import Area
from models.user import User
from api.v1.views import app_views
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt
from flask_jwt_extended import get_jwt_identity


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


@app_views.route('/regions/count', strict_slashes=False)
def region_count():
    """Returns the region count"""
    count = Region.count()
    return jsonify(region_count=count)


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


####################################################################################
####                            Admin regions Routes                            ####
####################################################################################
@app_views.route('/admin/regions', methods=['POST'], strict_slashes=False)
@jwt_required()
def add_region():
    """Add region (For Admin)"""
    claims = get_jwt()
    role = claims.get('role')
    if role != 'Admin':
        return jsonify(msg="Access forbidden"), 403
    data = request.get_json()
    name = data.get('name')
    region = Region.get_by_name(name)
    if region:
        return jsonify(message='Region already exist')
    region = Region(
        name=name
    )
    region.save()
    return jsonify(message='Region successfully added')

@app_views.route(
    '/admin/regions/<region_id>',
    methods=['DELETE', 'PATCH'],
    strict_slashes=False
)
@jwt_required()
def w_regions(region_id):
    """Delete/Update region route"""
    claims = get_jwt()
    role = claims.get('role')
    if role != 'Admin':
        return jsonify(msg="Access forbidden"), 403
    region = Region.get(region_id)
    if not region:
        return jsonify(message="Region Not Found"), 400
    if request.method == 'DELETE':
        region.delete()
        return jsonify(message='Successfully deleted')
    to_update = ['name']
    data = request.get_json()
    to_updates = region.get_infos_to_update(data, to_update)
    region.update(**to_updates)
    return jsonify(message='Succesfully updated')


@app_views.route(
    '/admin/regions/<region_id>/areas',
    methods=['POST'],
    strict_slashes=False
)
@jwt_required()
def add_area_to_region(region_id):
    """Add area to a region"""
    claims = get_jwt()
    role = claims.get('role')
    if role != 'Admin':
        return jsonify(msg="Access forbidden"), 403
    region = Region.get(region_id)
    if not region:
        return jsonify(message='Region Not Found'), 400

    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify(message='Missing name.'), 400

    if region.has('areas', name):
        return jsonify(message='Area already exist'), 400
    area = Area(
        name=name,
        region_id=region_id
    )
    area.save()
    return jsonify(message='Successfully added')
