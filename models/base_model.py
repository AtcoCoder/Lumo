"""Base Model module"""
from typing import List
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import datetime
import models
from sqlalchemy import String, DateTime
import uuid

DATETIME = '%Y-%m-%dT%H:%M:%S'
UTC = datetime.timezone.utc


class Base(DeclarativeBase):
    """declarative base class"""
    pass


class BaseModel(Base):
    """Base Model class"""
    # Mark as abstract so it doesn't create a table
    __abstract__ = True
    id = mapped_column(String(64), primary_key=True)
    created_at = mapped_column(DateTime, default=datetime.datetime.now(tz=UTC))
    updated_at = mapped_column(DateTime, default=datetime.datetime.now(tz=UTC))

    def __init__(self, **kwargs) -> None:
        """instance initializer"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now(tz=UTC)
        self.updated_at = datetime.datetime.now(tz=UTC)
        if kwargs:
            for key, value in kwargs.items():
                if key not in ['id', 'created_at', 'updated_at']:
                    setattr(self, key, value)
    
    def __str__(self) -> str:
        """String representation of the base model instance"""
        return '{:s} ({:s}) {}'.format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )
    
    def save(self):
        """adds instance object to the database"""
        models.db.add(self)
        models.db.save()

    def to_dict(self):
        """returns key/values pairs of the
        all instance attribute
        """
        instance_attrs = self.__dict__.copy()
        instance_attrs['__class__'] = self.__class__.__name__
        if 'password_hash' in instance_attrs:
            del instance_attrs['password_hash']
        if 'created_at' in instance_attrs:
            instance_attrs['created_at'] = instance_attrs['created_at'].strftime(DATETIME)
        if 'updated_at' in instance_attrs:
            instance_attrs['updated_at'] = instance_attrs['updated_at'].strftime(DATETIME)
        instance_attrs.pop('_sa_instance_state', None)
        return instance_attrs

    def delete(self):
        """delete instance object from database"""
        models.db.delete(self)
        models.db.save()

    def update(self, **kwargs):
        """Updates the attrs (keys) with the values
        provided in the kwargs
        """
        unchangeables = ['created_at','updated_at','id']
        for attr, new_value in kwargs.items():
            if attr not in unchangeables:
                setattr(self, attr, new_value)
            else:
                raise TypeError(f'Cannot change {attr}')
        self.updated_at = datetime.datetime.now(tz=UTC)
        models.db.save()
    
    def validate_value(self, attr, val_type, value):
        """Validates input value"""
        if type(value) != val_type:
            raise ValueError(f'{attr} must be {val_type}!')
    
    @classmethod
    def get(cls, id):
        """Gets object by id"""
        result = models.db.get(id, cls=cls)
        return result
    
    @classmethod
    def get_all(cls):
        result = models.db.all(cls)
        objs = [obj.to_dict() for obj in result]
        return objs
    
