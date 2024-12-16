"""User class Module"""
from typing import Any
from sqlalchemy import Column, String
from models.base_model import BaseModel


class User(BaseModel):
    """User class"""
    __tablename__ = 'users'
    username = Column(String(64), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    phone_number = Column(String(16), nullable=False)
    whatsapp = Column(String(16), nullable=True)
