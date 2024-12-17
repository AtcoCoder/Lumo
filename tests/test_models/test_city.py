"""Test City Module"""
import unittest
from models.city import City
from models.base_model import Base, BaseModel


class TestCity(unittest.TestCase):
    """Test suite for the city class"""
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up city object for tests"""
        cls.city = City()
    
    def test_city_superclasses(self):
        """Test that city is subclass of
        Base and BaseModel class
        """
        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(issubclass(City, Base))

    def test_city_attrs(self):
        """Test that city has right attrs"""
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'area_id'))
        self.assertTrue(hasattr(self.city, 'properties'))
    
    @classmethod
    def tearDownClass(cls) -> None:
        """Deletes city object after tests"""
        del cls.city
