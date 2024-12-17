"""User class Module"""
from typing import Any
from sqlalchemy import Column, String
from models.base_model import BaseModel

NOT_NULLABLES = [
    'password_hash',
    'email',
    'username',
    'phone_number'
]

# STRINGs = [
#     'email',
#     'username',
#     'phone_number'
#     'whatsapp'
# ]


class User(BaseModel):
    """User class"""
    __tablename__ = 'users'
    username = Column(String(64), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    phone_number = Column(String(16), nullable=False)
    whatsapp = Column(String(16), nullable=True)

    def __init__(self, **kwargs) -> None:
        """Instance Initializer"""
        for not_null in NOT_NULLABLES:
            if not_null not in kwargs:
                raise AttributeError('User must be created with a password')
        
        super().__init__(**kwargs)
        # for attr in STRINGs:
        #     if attr in kwargs:
        #         self.validate_value(attr, str, getattr(self, attr))
    
    @property
    def email(self):
        """Email getter method"""
        return self._email
    
    @email.setter
    def email(self, value):
        """Email setter"""
        self.validate_value('email', str, value)
        self._email = value

    @property
    def username(self):
        """Username getter method"""
        return self._username

    @username.setter
    def username(self, value):
        """Username setter"""
        self.validate_value('username', str, value)
        self._username = value
    
    @property
    def phone_number(self):
        """Getter method for phone number"""
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, value):
        """Setter for phone number"""
        self.validate_value('phone_number', str, value)
        self._phone_number = value
    
    @property
    def password_hash(self):
        """Getter for password_hash"""
        return self._password_hash

    @password_hash.setter
    def password_hash(self, value):
        """Setter for password_hash"""
        self.validate_value('password_hash', str, value)
        self._password_hash = value
    
    @property
    def whatsapp(self):
        """Getter for whatsapp property"""
        return self._whatsapp
    
    @whatsapp.setter
    def whatsapp(self, value):
        """Setter for whatsapp"""
        self.validate_value('whatsapp', str, value)
        self._whatsapp = value
