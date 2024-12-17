from models.area import Area
from models.base_model import BaseModel
import unittest


class TestArea(unittest.TestCase):
    """Test suite for Area class"""
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up area object for tests"""
        cls.area = Area()
    
    def test_area_superclass(self):
        """Test that area is a subclass
        of BaseModel class"""
        self.assertTrue(issubclass(Area, BaseModel))
    
    def test_area_attrs(self):
        """Test that area has all attrs"""
        self.assertTrue(hasattr(self.area, 'id'))
        self.assertTrue(hasattr(self.area, 'created_at'))
        self.assertTrue(hasattr(self.area, 'updated_at'))
        self.assertTrue(hasattr(self.area, 'name'))
        self.assertTrue(hasattr(self.area, 'cities'))
        self.assertTrue(hasattr(self.area, 'region_id'))
    
    @classmethod
    def tearDownClass(cls) -> None:
        """Deletes the area object after
        all tests"""
        del cls.area
