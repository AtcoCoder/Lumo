"""db module"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

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
        from models.user import User
        from models.property import Property
        from models.city import City
        from models.area import Area
        from models.region import Region
        from models.amenity import Amenity
        from models.image import Image
        classes = {
            'User': User,
            'Property': Property,
            'City': City,
            'Area': Area,
            'Region': Region,
            'Amenity': Amenity,
            'Image': Image
        }
        if cls:
            objs = self.__session.query(classes[cls]).all()
        return objs
    
    def add(self, obj):
        """Add object (obj) to the session
        """
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
    
    def get(self, cls, id):
        """Finds and returns an object base id
        """
        user = self.__session.query(cls).filter_by(id=id).first()
        return user
    
    def count(self, cls=None):
        """Count the number of members of 
        table(cls) and return the number
        """
        results = self.all(cls)
        return len(results)
