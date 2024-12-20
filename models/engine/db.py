"""db module"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.orm import aliased
from models.user import User
from models.property import Property
from models.city import City
from models.area import Area
from models.region import Region
from models.amenity import Amenity
from models.image import Image
from config import CURRENT_CONFIG
classes = {
    'User': User,
    'Property': Property,
    'City': City,
    'Area': Area,
    'Region': Region,
    'Amenity': Amenity,
    'Image': Image
}

class_list = [User, Property, City, Area, Region, Amenity, Image]

# URL = DevelopmentConfig.DATABASE_URI


class DB():
    """Database class"""
    __session = None
    __engine = None
    def __init__(self, db_url) -> None:
        """Instance Initializer"""
        self.__engine = create_engine(db_url)
    
    @property
    def session(self):
        """Returns database session"""
        return self.__session

    def reload(self):
        """reloads the database and creates scoped session"""
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        sessn_factory = sessionmaker(bind=self.__engine)
        Session = scoped_session(sessn_factory)
        self.__session = Session

    def all(self, cls=None):
        """returns all members of every table if
        no table is specified else all
        members of the table specified
        """ 
        if cls:
            objs = self.__session.query(cls).all()

            return objs
        else:
            raise TypeError('Class must be specified')
    
    def add(self, obj=None):
        """Add object (obj) to the session
        """
        if not obj:
            raise TypeError('Object cannot be none')
        valid_obj = [obj for cls in class_list if isinstance(obj, cls)]
        if not valid_obj:
            raise TypeError('Not a valid object')
        self.__session.add(obj)
    
    def save(self):
        """Commit all changes of the current session
        """
        self.__session.commit()

    def close(self):
        """Closes the current session
        """
        self.__session.close()
        self.__session.remove()
    
    def get(self, id, cls=None):
        """Finds and returns an object base id
        """
        if not cls:
            raise TypeError('Class cannot be None')
        if not isinstance(id, str):
            raise TypeError('id must be a string')
        

        result = self.__session.query(cls).filter_by(id=id).first()
        return result
    
    def count(self, cls=None):
        """Count the number of members of 
        table(cls) and return the number
        """
        results = self.all(cls)
        return len(results)
    
    def get_by(self, column, value):
        """Gets user by email or username"""
        if column == 'email':
            result = self.__session.query(User).filter_by(email=value).first()
        else:
            result = self.__session.query(User).filter_by(username=value).first()
        return result
    
    def delete(self, obj):
        """Deletes object from the database"""
        try:
            self.__session.delete(obj)
        except Exception:
            pass
    
    def drop(self):
        """Drops all tables"""
        if CURRENT_CONFIG.TESTING:
            from models.base_model import Base
            Base.metadata.drop_all(bind=self.__engine)

