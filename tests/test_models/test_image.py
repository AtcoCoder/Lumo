"""image Class Unit Test"""
import unittest
from models.image import Image
from models.base_model import BaseModel


class TestImage(unittest.TestCase):
    """Unit test for image class"""
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up image instance"""
        cls.image = Image()
    
    def test_image_superclass(self):
        """Test that image is subclass of
        basemodel class"""
        self.assertTrue(issubclass(Image, BaseModel))
    
    def test_image_attrs(self):
        """Test that images has all
        attrs"""
        self.assertTrue(hasattr(self.image, 'id'))
        self.assertTrue(hasattr(self.image, 'created_at'))
        self.assertTrue(hasattr(self.image, 'updated_at'))
        self.assertTrue(hasattr(self.image, 'image_url'))
        self.assertTrue(hasattr(self.image, 'property_id'))
    
    def test_image_upload_time(self):
        """Test that image upload time
        is the same as created_at time"""
        self.assertEqual(self.image.created_at, self.image.uploaded_at)
    
    @classmethod
    def tearDownClass(cls) -> None:
        """Deletes image instance after all tests"""
        del cls.image
