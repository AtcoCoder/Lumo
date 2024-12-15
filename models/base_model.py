"""Base Model module"""
from sqlalchemy.orm import DeclarativeBase
import datetime
from sqlalchemy import Column, String, DateTime
import uuid

UTC = datetime.timezone.utc


class Base(DeclarativeBase):
    """declarative base class"""
    pass


class BaseModel:
    """Base Model class"""
    id = Column(String(64), primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now(tz=UTC))
    updated_at = Column(DateTime, default=datetime.datetime.now(tz=UTC))

    def __init__(self) -> None:
        """instance initializer"""
        self.id = str(uuid.uuid4())
    
    def __str__(self) -> str:
        """String representation of the base model instance"""
        return "{:s} ({:s}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )
    
    def save(self):
        """adds instance object to the database"""
        pass

    def to_dict(self):
        """returns key/values pairs of the
        all instance attribute
        """
        instance_attrs = self.__dict__.copy()
        return instance_attrs

    def delete(self):
        """delete instance object from database"""
        pass
