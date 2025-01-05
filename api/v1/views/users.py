"""User views module"""
from api.v1.views import app_views
from flask import jsonify, request
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.image import Image
from models.blocked_token import BlockedToken
from models.property import Property
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt
from werkzeug.security import (
    generate_password_hash,
)

@app_views.route('/users', strict_slashes=False)
def get_users():
    """Returns all users"""
    users = User.get_all()
    return jsonify(users=users)


@app_views.route('/auth/signup', methods=['POST'], strict_slashes=False)
def register_user():
    """Register user account"""
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    phone_number = data.get('phone_number')
    whatsapp = data.get('whatsapp')
    user = User.get_by_email(email)
    if user:
        return jsonify({'message': 'User already exist'}), 400
    
    user = User.get_by_username(username)
    if user:
        return jsonify(message='Username already taken'), 400
    
    if not password or not email or not username or not phone_number:
        return jsonify(message='Missing field'), 400
    password_hash = generate_password_hash(
        password=password,
        method='pbkdf2:sha256',
        salt_length=8
    )
    try:
        user = User(
            email=email,
            username=username,
            password_hash=password_hash,
            phone_number=phone_number,
            whatsapp=whatsapp
        )
    except (AttributeError, ValueError):
        return jsonify({'message': 'Invalid'}), 400
    user.save()
    return jsonify(message='User successfully created.'), 201


@app_views.route('/users/<user_id>', strict_slashes=False)
def get_user(user_id):
    """Get user by id (user_id) (For admin and others)"""
    user = User.get(user_id)
    if not user:
        return jsonify(message='User not Found'), 400
    return jsonify(user=user.to_dict_with('properties', user.properties))

@app_views.route(
    '/auth/login',
    strict_slashes=False,
    methods=['POST']
)
def user_login():
    """User Login"""
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if email and password:
        user = User.get_by_email(email)
    else:
        return jsonify(message='Missing field'), 400
    if not user:
        return jsonify(message='User does not exist'), 400
    if user.is_valid(password):
        role = 'User'
        if email == 'admin@email.com':
            role = 'Admin'
        access_token = create_access_token(
            identity=user.username,
            fresh=True,
            additional_claims={'role': role}
        )
        refresh_token = create_refresh_token(
            identity=user.username,
            additional_claims={'role': role}
        )
        return jsonify(access_token=access_token, refresh_token=refresh_token)
    return jsonify(message='Incorrect password')


@app_views.route(
    '/auth/logout',
    strict_slashes=False,
    methods=['POST']
)
@jwt_required()
def user_logout():
    """Logout route"""
    jti = get_jwt()['jti']
    blocked_token = BlockedToken(
        jti=jti
    )
    blocked_token.save()
    return jsonify(message='Successfully logged out!!')
    

@app_views.route(
    'auth/refresh',
    strict_slashes=False,
    methods=['POST']
)
@jwt_required(refresh=True)
def refresh():
    """Refresh authentication token"""
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity, fresh=False)
    return jsonify(access_token=access_token)


@app_views.route(
        'users/me',
        strict_slashes=False,
        methods=['GET', 'PATCH', 'DELETE']
)
@jwt_required()
def get_me():
    """Get/update/delete current authenticated user"""
    username = get_jwt_identity()
    user = User.get_by_username(username)
    if not user:
        return jsonify(message='Not found'), 400

    if request.method == 'PATCH':
        can_updates = [
            'email',
            'username',
            'password',
            'phone_number',
            'whatsapp'
        ]
        to_updates = user.get_infos_to_update(request.get_json(), can_updates)
        user.update(**to_updates)
        if username != user.username:
            access_token = create_access_token(identity=user.username, fresh=True)
            refresh_token = create_refresh_token(identity=user.username)
            return jsonify(access_token=access_token, refresh_token=refresh_token)
        return jsonify(message='User successfully updated')

    if request.method == 'DELETE':
        user.delete()
        jti = get_jwt()['jti']
        print('jti:', jti)
        blocked_token = BlockedToken(
            jti=jti
        )
        blocked_token.save()
        return jsonify(message='User deleted successfully')

    user_dict = user.to_dict_with('properties', user.properties)
    return jsonify(me=user_dict)




@app_views.route(
    '/users/<user_id>',
    methods=['PATCH', 'DELETE'],
    strict_slashes=False
)
@jwt_required()
def update_delete_user(user_id):
    """Update/delete user (For admin)"""
    claims = get_jwt()
    role = claims.get('role')
    if role != 'Admin':
        return jsonify(msg="Access forbidden"), 403
    user = User.get(user_id)
    if not user:
        return jsonify(message='User not found'), 400
    if request.method == 'DELETE':
        user.delete()
        return jsonify(message='User deleted successfully')
    can_updates = [
        'email',
        'username',
        'password',
        'phone_number',
        'whatsapp'
    ]
    to_updates = user.get_infos_to_update(request.get_json(), can_updates)
    user.update(**to_updates)
    return jsonify(message='User successfully updated')


@app_views.route('/protected')
@jwt_required()
def protected():
    return jsonify(hello='world')


@app_views.route('/properties', methods=['POST'], strict_slashes=False)
@jwt_required()
def add_property():
    """Add a property"""
    identity = get_jwt_identity()
    user = User.get_by_username(identity)
    if not user:
        return jsonify(message="Can't add property"), 400
    data = request.get_json()
    title = data.get('title')
    price = data.get('price')
    description = data.get('description')
    property_type = data.get('property_type')
    city_id = data.get('city_id')
    amenity_ids = data.get('amenities', [])
    image_list = data.get('images')
    amenities = [Amenity.get(amenity_id) for amenity_id in amenity_ids]
    if None in [
        title,
        price,
        description,
        property_type,
        city_id,
    ]:
        return jsonify(message='Missing field.'), 400

    city = City.get(city_id)
    if not city:
        return jsonify(message='City not Found')
    location = city.return_location()
    city_id = city.id
    property = Property(
        title=title,
        price=price,
        location=location,
        description=description,
        property_type=property_type,
        is_active=True,
        amenities=amenities,
        user_id=user.id,
        city_id =city_id
    )
    images = [Image(image_url=image_url) for image_url in image_list]
    property.images = images
    property.save()
    return jsonify(message='Property succesfully added.')


@app_views.route(
    '/properties/<property_id>',
    strict_slashes=False,
    methods=['PATCH', 'DELETE']
)
@jwt_required()
def w_property(property_id):
    """Update/delete property"""
    identity = get_jwt_identity()
    user = User.get_by_username(identity)
    claims = get_jwt()
    role = claims.get('role')
    if role != 'Admin' and not user:
        return jsonify(message='User not found'), 400
    property = Property.get(property_id)
    if not property:
        return jsonify(message='Property not found'), 400
    
    if request.method == 'PATCH':
        data = request.get_json()
        can_updates = [
            'price',
            'title',
            'description',
            'property_type',
            'is_active'
        ]
        updates = property.get_infos_to_update(data, can_updates)
        property.update(**updates)
        return jsonify(message='Succesfully updated.')
    property.delete()
    return jsonify(message='Property deleted')


@app_views.route(
    '/users/<user_id>/properties',
    strict_slashes=False
)
def get_user_properties(user_id):
    """Get a user's properties"""
    user = User.get(user_id)
    if not user:
        return jsonify(message='User Not Found.'), 400
    properties = user.properties
    property_list = []
    for property in properties:
        property_dict = property.to_dict_with('amenities', property.amenities)
        property_dict['images'] = property.its('images')
        property_list.append(property_dict)
    return jsonify(properties=property_list)


@app_views.route(
    '/users/me/properties',
    strict_slashes=False
)
@jwt_required()
def get_current_user_properties():
    """Get current authenticated user's properties"""
    username = get_jwt_identity()
    user = User.get_by_username(username)
    if not user:
        return jsonify(message='User Not Found.'), 400
    properties = user.properties
    property_list = []
    for property in properties:
        property_dict = property.to_dict_with('amenities', property.amenities)
        property_dict['images'] = property.its('images')
        property_list.append(property_dict)
    return jsonify(properties=property_list)
