from models.amenity import Amenity
from models.base_model import Base
import unittest


class TestAmenity(unittest.TestCase):
    """Test suite for Amenity class"""
    @classmethod
    def setUpClass(cls) -> None:
        """Set up amenity object for testing"""
        cls.amenity = Amenity()
    
    def test_amenity_superclass(self):
        """Test that amenity is subclass of
        Base
        """
        self.assertTrue(issubclass(Amenity, Base))
    
    def test_amenity_attrs(self):
        """Test that amenity has right attrs"""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'properties'))
