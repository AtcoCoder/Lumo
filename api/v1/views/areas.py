"""Area views module"""
from models.area import Area
from flask import request, jsonify
from api.v1.views import app_views
from models.region import Region


@app_views.route(
    '/areas/add',
    methods=['POST'],
    strict_slashes=False
)
def add_area():
    """Adds area to database"""
    name = request.form.get('name')
    region_name = request.form.get('region_name')
    region = Region.get_by_name(region_name)
    if not region:
        return jsonify(message='Region Not Found'), 400
    area = Area(
        name=name,
        region_id=region.id
    )
    return jsonify(message='Area succesfully added')
    