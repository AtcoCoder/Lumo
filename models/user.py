"""User class Module"""
from typing import Any, List
from sqlalchemy import Column, String
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
import datetime
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from flask_login import UserMixin


DATETIME = '%Y-%m-%dT%H:%M:%S'
UTC = datetime.timezone.utc

NOT_NULLABLES = [
    'password_hash',
    'email',
    'username',
    'phone_number'
]

STRINGs = [
    'email',
    'username',
    'phone_number',
    'whatsapp'
]


class User(BaseModel):
    """User class"""
    __tablename__ = 'users'
    username = mapped_column(String(64), nullable=False, unique=True)
    email = mapped_column(String(128), nullable=False, unique=True)
    password_hash = mapped_column(String(255), nullable=False)
    phone_number = mapped_column(String(16), nullable=False)
    whatsapp = mapped_column(String(16), nullable=True)
    properties = relationship('Property', backref='user')
    is_authenticated = False
    is_active = False
    is_anonymous = True

    def __init__(self, **kwargs) -> None:
        """Instance Initializer"""
        for not_null in NOT_NULLABLES:
            if not_null not in kwargs:
                raise AttributeError('User must be created with a password')
        
        for attr in STRINGs:
            if attr in kwargs:
                value = kwargs[attr]
                if attr == 'whatsapp' and kwargs[attr] is None:
                    value = 'null'
                self.validate_value(attr, str, value)
        super().__init__(**kwargs)

    def is_valid(self, password):
        """Verifies password"""
        return check_password_hash(self.password_hash, password)
    
    def login(self, email, password):
        """Logs user in"""
        pass
    
    @classmethod
    def get_by_email(self, email):
        """Gets user by email"""
        import models
        return models.db.get_by(self, email, 'email')
    
    @classmethod
    def get_by_username(self, username):
        """Gets user by username"""
        import models
        return models.db.get_by(self, username, 'username')

    def update(self, **kwargs):
        """Updates the attrs (keys) with the values
        provided in the kwargs
        """
        import models
        unchangeables = ['created_at','updated_at','id']
        for attr, new_value in kwargs.items():
            if attr not in unchangeables:
                if attr == 'password':
                    attr = 'password_hash'
                    new_value = generate_password_hash(
                        password=new_value,
                        method='pbkdf2:sha256',
                        salt_length=8
                    )
                setattr(self, attr, new_value)
            else:
                raise TypeError(f'Cannot change {attr}')
        self.updated_at = datetime.datetime.now(tz=UTC)
        models.db.save()
    
    def get_id(self):
        """Returns user id"""
        return self.id
    
    @property
    def is_authenticated(self):
        """Indicate that user is authenticated"""
        return True
    
    @property
    def is_active(self):
        """Indicate the user is active"""
        return True

    @property
    def is_anonymous(self):
        """Indicates that the user is anonymous"""
        return False
    
    # # @property
    # # def email(self):
    # #     """Email getter method"""
    # #     return self._email
    
    # @email.setter
    # def email(self, value):
    #     """Email setter"""
    #     self.validate_value('email', str, value)
    #     self.email = value

    # @property
    # def username(self):
    #     """Username getter method"""
    #     return self._username

    # @username.setter
    # def username(self, value):
    #     """Username setter"""
    #     self.validate_value('username', str, value)
    #     self._username = value
    
    # @property
    # def phone_number(self):
    #     """Getter method for phone number"""
    #     return self._phone_number
    
    # @phone_number.setter
    # def phone_number(self, value):
    #     """Setter for phone number"""
    #     self.validate_value('phone_number', str, value)
    #     self._phone_number = value
    
    # @property
    # def password_hash(self):
    #     """Getter for password_hash"""
    #     return self._password_hash

    # @password_hash.setter
    # def password_hash(self, value):
    #     """Setter for password_hash"""
    #     self.validate_value('password_hash', str, value)
    #     self._password_hash = value
    
    # # @property
    # # def whatsapp(self):
    # #     """Getter for whatsapp property"""
    # #     return self._whatsapp
    
    # # @whatsapp.setter
    # # def whatsapp(self, value):
    # #     """Setter for whatsapp"""
    # #     self.validate_value('whatsapp', str, value)
    # #     self._whatsapp = value
