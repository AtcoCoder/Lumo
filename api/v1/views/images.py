from api.v1.views import app_views
from models.user import User
from models.property import Property
from models.image import Image
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity


@app_views.route(
    '/images/<image_id>',
    strict_slashes=False,
    methods=['DELETE']
)
@jwt_required()
def delete_image(image_id):
    """Update"""
    username = get_jwt_identity()
    user = User.get_by_username(username)
    if not user:
        return jsonify(message='User not found'), 400
    image = Image.get(image_id)
    if not image:
        return jsonify(message='Image not found'), 400
    property = Property.get(image.property_id)
    if not property:
        return jsonify(messge='Property not found'), 400
    if user.id != property.user_id:
        return jsonify(message='Unauthorized User'), 403
    image.delete()
    return jsonify(message='Image successfully deleted.')


####################################################################################
####                            Admin Users Routes                              ####
####################################################################################

@app_views.route(
    '/admin/images/<image_id>',
    strict_slashes=False,
    methods=['DELETE']
)
@jwt_required()
def admin_delete_image(image_id):
    """Delete image by admin"""
    claims = get_jwt()
    role = claims.get('role')
    if role != 'Admin':
        return jsonify(msg="Access forbidden"), 403
    image = Image.get(image_id)
    if not image:
        return jsonify(message='Image not found'), 400
    image.delete()
    return jsonify(message='Image successfully deleted.')
