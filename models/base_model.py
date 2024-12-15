"""Base Model module"""
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """declarative base class"""
    pass


class BaseModel:
    """Base Model class"""
