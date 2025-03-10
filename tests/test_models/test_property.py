from models.property import Property
from models.base_model import BaseModel
import unittest

TITLE = 'A new house'
USER_ID = 'user_Id_user_Id_user_Id'
PRICE = 100.00
LOCATION = 'West Coast Region, Kombo Area, Busumbala'
PROPERTY_TYPE = 'sale'
CITY_ID = 'city_id_city_id_city_id'
SIZE = 100


class TestProperty(unittest.TestCase):
    """Property class test suite"""
    @classmethod
    def setUpClass(cls) -> None:
        cls.property = Property(
            title=TITLE,
            user_id=USER_ID,
            price=PRICE,
            location=LOCATION,
            size=SIZE
        )
    
    def test_property_superclass(self):
        """Test that property is a subclass
        of the base model
        """
        pass

    def test_property_missing_title(self):
        """Test that property has title
        provided
        """
        with self.assertRaises(AttributeError):
            Property()
    
    def test_property_missing_user_id(self):
        """Test that property has user_id"""
        with self.assertRaises(AttributeError):
            Property(
                title=TITLE
            )
    
    def test_property_missing_price(self):
        """Test that property has missing price"""
        with self.assertRaises(AttributeError):
            Property(
                title=TITLE,
                user_id=USER_ID
            )
    
    def test_property_missing_location(self):
        """Test that property has location"""
        with self.assertRaises(AttributeError):
            Property(
                title=TITLE,
                user_id=USER_ID,
                price=PRICE
            )
    
    def test_property_missing_size(self):
        """Test that property has size"""
        with self.assertRaises(AttributeError):
            Property(
                title=TITLE,
                user_id=USER_ID,
                price=PRICE,
                location=LOCATION
            )
    
    def test_property_superclass(self):
        """Test that BaseModel is superclass
        of Property"""
        self.assertTrue(issubclass(Property, BaseModel))
    
    def test_title_attr(self):
        """Test that property has title attr"""
        self.assertTrue(hasattr(self.property, 'title'))
    
    def test_property_attrs(self):
        """Test that property has all attrs"""
        self.assertTrue(hasattr(self.property, 'description'))
        self.assertTrue(hasattr(self.property, 'price'))
        self.assertTrue(hasattr(self.property, 'location'))
        self.assertTrue(hasattr(self.property, 'property_type'))
        self.assertTrue(hasattr(self.property, 'is_active'))
        self.assertTrue(hasattr(self.property, 'created_at'))
        self.assertTrue(hasattr(self.property, 'updated_at'))
        self.assertTrue(hasattr(self.property, 'size'))
        self.assertTrue(hasattr(self.property, 'city_id'))
        self.assertTrue(hasattr(self.property, 'user_id'))
        self.assertTrue(hasattr(self.property, 'amenities'))
        self.assertTrue(hasattr(self.property, 'images'))
    
    @classmethod
    def tearDownClass(cls) -> None:
        """tear down after tests"""
        del cls.property
