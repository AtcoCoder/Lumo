"""db module"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


URL = ""

class DB():
    """Database class"""
    __session = None
    __engine = None
    def __init__(self) -> None:
        """Instance Initializer"""
        self.__engine = create_engine(URL)

    def all(self, cls=None):
        """returns all members of every table if
        no table is specified else all
        members of the table specified
        """
        return None
    
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
        self.__session.remove()
    
    def get(self, cls, id):
        """Finds and returns an object base id
        """
        return None
    
    def count(self):
        """Count the number of members of 
        table(cls) and return the number
        """
        return 0
