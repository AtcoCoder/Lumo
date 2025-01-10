from api.v1.views import app_views
from models.image import Image
from flask import jsonify


@app_views.route(
    '/images/<image_id>',
    strict_slashes=False,
    methods=['DELETE']
)
def delete_image(image_id):
    """Update"""
    image = Image.get(image_id)
    if not image:
        return jsonify(message='Image not found'), 400
    image.delete()
    return jsonify(message='Image successfully deleted.')