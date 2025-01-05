"""Area views module"""
from models.area import Area
from models.city import City
from flask import request, jsonify
from api.v1.views import app_views
from models.region import Region
from flask_jwt_extended import jwt_required, get_jwt


# @app_views.route(
#     '/areas/add',
#     methods=['POST'],
#     strict_slashes=False
# )
# def add_area():
#     """Adds area to database"""
#     name = request.form.get('name')
#     region_name = request.form.get('region_name')
#     region = Region.get_by_name(region_name)
#     if not region:
#         return jsonify(message='Region Not Found'), 400
#     if not name:
#         return jsonify(message='Missing name')
#     area = Area.get_by_name(name)
#     if area:
#         return jsonify(message='Area already exist'), 400
#     area = Area(
#         name=name,
#         region_id=region.id
#     )
#     area.save()
#     return jsonify(message='Area succesfully added')
    

@app_views.route(
    '/areas',
    strict_slashes=False
)
def all_areas():
    """All areas route"""
    areas = Area.get_all()
    return jsonify(areas=areas)

@app_views.route('/areas/<area_id>', strict_slashes=False)
def get_area(area_id):
    """Get region route"""
    area = Area.get(area_id)
    if not area:
        return jsonify(message="Area Not Found"), 400
    return jsonify(area=area.to_dict_with('cities', area.cities))


@app_views.route(
    '/areas/<area_id>',
    methods=['DELETE', 'PATCH'],
    strict_slashes=False
)
@jwt_required()
def w_areas(area_id):
    """Delete/Update area route"""
    claims = get_jwt()
    role = claims.get('role')
    if role != 'Admin':
        return jsonify(msg="Access forbidden"), 403
    area = Area.get(area_id)
    if not area:
        return jsonify(message="Area Not Found"), 400
    if request.method == 'DELETE':
        area.delete()
        return jsonify(message='Successfully deleted')
    to_update = ['name']
    to_updates = area.get_infos_to_update(request.get_json(), to_update)
    area.update(**to_updates)
    return jsonify(message='Succesfully updated')



@app_views.route(
    '/areas/<area_id>/cities',
    strict_slashes=False
)
def get_area_cities(area_id):
    """Get area cities route"""
    area = Area.get(area_id)
    if not area:
        return jsonify(message='Area Not Found'), 400
    cities = area.its('cities', 'properties')
    return jsonify(cities=cities)

@app_views.route(
    'areas/<area_id>/cities',
    methods=['POST'],
    strict_slashes=False
)
@jwt_required()
def add_area_city(area_id):
    """Add city route"""
    claims = get_jwt()
    role = claims.get('role')
    if role != 'Admin':
        return jsonify(msg="Access forbidden"), 403
    area = Area.get(area_id)
    if not area:
        return jsonify(message='Area Not Found'), 400
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify(message='Missing name.')
    if area.has('cities', name):
        return jsonify(message='City already exist')
    city = City(
        name=name,
        area_id=area_id
    )
    city.save()
    return jsonify(message='City successfully created')
