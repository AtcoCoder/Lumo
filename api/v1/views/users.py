"""User views module"""
from api.v1.views import app_views
from flask import jsonify, request
from models.user import User
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

@app_views.route('/users')
def get_users():
    """Returns all users"""
    users = User.get_all()
    return jsonify(users=users)


@app_views.route('/register', methods=['GET', 'POST'])
def register_user():
    """Register user account"""
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        phone_number = request.form.get('phone_number')
        whatsapp = request.form.get('whatsapp')
    user = User.get_by_email(email)
    if user:
        return jsonify({'message': 'User already exist'}), 400
    
    user = User.get_by_username(username)
    if user:
        return jsonify(message='Username already taken'), 400
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
    except AttributeError:
        return jsonify({'message': 'Invalid'}), 400
    user.save()
    return jsonify(message='User successfully created.'), 201
