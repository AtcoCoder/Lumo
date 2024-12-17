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

STRINGs = [
    'email',
    'username',
    'phone_number',
    'whatsapp'
]


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
        for attr in STRINGs:
            if attr in kwargs:
                self.validate_value(attr, str, getattr(self, attr))

