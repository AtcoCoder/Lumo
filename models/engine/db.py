"""db module"""
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError, InvalidRequestError
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
from models.blocked_token import BlockedToken
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

class_list = [User, Property, City, Area, Region, Amenity, Image, BlockedToken]

# URL = DevelopmentConfig.DATABASE_URI


class DB():
    """Database class"""
    __engine = None
    def __init__(self, db_url) -> None:
        """Instance Initializer"""
        self.__engine = create_engine(
            db_url,
            pool_size=20,
            max_overflow=5,
            pool_recycle=3600,
            pool_timeout=30
        )

    def check_session(self):
        """Ensure the is active."""
        try:
            self.__session.execute(text("SELECT 1"))
        except (OperationalError, InvalidRequestError):
            self.__session.rollback()
            self.__session.close()
            self.reload()

    def rollback_on_error(self):
        """Rollback the session if it's in a pending state."""
        try:
            self.__session.rollback()
        except InvalidRequestError:
            pass
    
    @property
    def session(self):
        """Returns database session"""
        return self.__session
    
    @property
    def engine(self):
        """Returns database engine"""
        return self.__engine

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
            self.check_session()

            try:
                objs = self.__session.query(cls).all()

                return objs
            except OperationalError as e:
                self.rollback_on_error()
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
        self.check_session()
        try:
            self.__session.add(obj)
        except OperationalError as e:
            self.rollback_on_error()
            raise e
    
    def save(self):
        """Commit all changes of the current session
        """
        self.check_session()
        try:
            self.__session.commit()
        except OperationalError as e:
            self.rollback_on_error()
            raise e

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
        

        self.check_session()
        try:
            result = self.__session.query(cls).filter_by(id=id).first()
            return result
        except OperationalError as e:
            self.rollback_on_error()
            raise e
    
    def count(self, cls=None):
        """Count the number of members of 
        table(cls) and return the number
        """
        self.check_session()
        try:
            results = self.all(cls)
            return len(results)
        except OperationalError as e:
            self.rollback_on_error()
            raise e
    
    def get_by(self, cls, value, column=None):
        """Gets user by email or username"""
        self.check_session()
        try:
            if not column:
                result = self.__session.query(cls).filter_by(name=value).first()
            elif column == 'email':
                result = self.__session.query(User).filter_by(email=value).first()
            elif column == 'username':
                result = self.__session.query(User).filter_by(username=value).first()
            else:
                result = self.__session.query(BlockedToken).filter_by(jti=value).first()
            return result
        except OperationalError as e:
            self.rollback_on_error()
            raise e
    
    def delete(self, obj):
        """Deletes object from the database"""
        self.check_session()
        try:
            self.__session.delete(obj)
        except OperationalError as e:
            self.rollback_on_error()
            raise e
    
    def drop(self):
        """Drops all tables"""
        if CURRENT_CONFIG.TESTING:
            from models.base_model import Base
            Base.metadata.drop_all(bind=self.__engine)

