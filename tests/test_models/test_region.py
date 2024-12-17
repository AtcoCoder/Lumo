"""Region Class Unit Test"""
import unittest
from models.region import Region
from models.base_model import BaseModel


class TestRegion(unittest.TestCase):
    """Unit test for region class"""
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up region instance"""
        cls.region = Region()
    
    def test_region_superclass(self):
        """Test that region is subclass of
        basemodel class"""
        self.assertTrue(issubclass(Region, BaseModel))
    
    def test_region_attrs(self):
        """Test that regions has all
        attrs"""
        self.assertTrue(hasattr(self.region, 'id'))
        self.assertTrue(hasattr(self.region, 'created_at'))
        self.assertTrue(hasattr(self.region, 'updated_at'))
        self.assertTrue(hasattr(self.region, 'name'))
        self.assertTrue(hasattr(self.region, 'areas'))
    
    @classmethod
    def tearDownClass(cls) -> None:
        """Deletes region instance after all tests"""
        del cls.region
