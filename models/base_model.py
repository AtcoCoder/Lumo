"""Base Model module"""
from typing import List
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import datetime
import models
from sqlalchemy import String, DateTime
from sqlalchemy import MetaData
import uuid

DATETIME = '%Y-%m-%dT%H:%M:%S'
UTC = datetime.timezone.utc
metadata = MetaData()


class Base(DeclarativeBase):
    """declarative base class"""
    metadata = metadata


class BaseModel(Base):
    """Base Model class"""
    # Mark as abstract so it doesn't create a table
    __abstract__ = True
    id = mapped_column(String(64), primary_key=True)
    created_at = mapped_column(DateTime, nullable=False, default=datetime.datetime.now(tz=UTC))
    updated_at = mapped_column(DateTime, nullable=False, default=datetime.datetime.now(tz=UTC))

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
        relationship_dict = {
            'Region': ['areas'],
            'Area': ['cities'],
            'City': ['properties'],
            'User': ['properties'],
            'Property': ['images', 'amenities'],
            'Amenity': ['properties']
        }
        result = models.db.all(cls)
        objs = []
        for obj in result:
            relationships = relationship_dict[obj.__class__.__name__]
            obj_dict = obj.to_dict()
            for relationship in relationships:
                obj_dict[relationship] = obj.its(relationship)
            objs.append(obj_dict)
        return objs
    

    def get_infos_to_update(self, data, can_updates):
        """Returns dict of attrs to be updated
        with the values to update with"""
        to_update = {}
        attrs = {}
        for can_update in can_updates:
            attrs[can_update] = data.get(can_update)
        for attr, value in attrs.items():
            if value:
                to_update[attr] = value
        return to_update
        
    @classmethod
    def get_by_name(cls, name):
        """Finds place by name"""
        result = models.db.get_by(cls, name)
        return result
    
    def to_dict_with(self,relationship ,obj_list):
        """Turns objects of list into json
        serializable"""
        obj_dict = self.to_dict()
        obj_dict_list = []
        for obj in obj_list:
            obj_dict_list.append(obj.to_dict())
        obj_dict[relationship] = obj_dict_list
        return obj_dict

    def its(self, children, g_children=None):
        """returns serialized children list"""
        children_list = getattr(self, children)
        s_list = []
        g_children_list = []
        for child in children_list:
            if g_children:
                g_children_list = getattr(child, g_children)
                s_list.append(child.to_dict_with(g_children, g_children_list))
            s_list.append(child.to_dict())
        return s_list

