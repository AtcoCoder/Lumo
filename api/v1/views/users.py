"""User views module"""
from api.v1.views import app_views
from flask import jsonify, request
from models.user import User
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

@app_views.route('/users', strict_slashes=False)
def get_users():
    """Returns all users"""
    users = User.get_all()
    return jsonify(users=users)


@app_views.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register_user():
    """Register user account"""
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        phone_number = request.form.get('phone_number')
        whatsapp = request.form.get('whatsapp')
        print(request.form)
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
    """Get user by id (user_id)"""
    user = User.get(user_id)
    if not user:
        return jsonify(message='User not Found'), 400
    return jsonify(user=user.to_dict())
