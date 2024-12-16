"""Base Model module"""
from sqlalchemy.orm import DeclarativeBase
import datetime
from sqlalchemy import Column, String, DateTime
import uuid

UTC = datetime.timezone.utc


class Base(DeclarativeBase):
    """declarative base class"""
    pass


class BaseModel(Base):
    """Base Model class"""
    # Mark as abstract so it doesn't create a table
    __abstract__ = True
    id = Column(String(64), primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now(tz=UTC))
    updated_at = Column(DateTime, default=datetime.datetime.now(tz=UTC))

    def __init__(self) -> None:
        """instance initializer"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now(tz=UTC)
        self.updated_at = datetime.datetime.now(tz=UTC)
    
    def __str__(self) -> str:
        """String representation of the base model instance"""
        return '{:s} ({:s}) {}'.format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )
    
    def save(self):
        """adds instance object to the database"""
        #db.add(self)
        #db.save()

    def to_dict(self):
        """returns key/values pairs of the
        all instance attribute
        """
        instance_attrs = self.__dict__.copy()
        instance_attrs['__class__'] = self.__class__.__name__
        if 'password' in instance_attrs:
            del instance_attrs['password']
        instance_attrs.pop('_sa_instance_state', None)
        return instance_attrs

    def delete(self):
        """delete instance object from database"""
        #db.delete(self)

    def update(self, **kwargs):
        """Updates the attrs (keys) with the values
        provided in the kwargs
        """
        unchangeables = ['created_at','updated_at','id']
        for attr, new_value in kwargs.items():
            if attr not in unchangeables:
                setattr(self, attr, new_value)
        self.updated_at = datetime.datetime.now(tz=UTC)
        # db.save()
