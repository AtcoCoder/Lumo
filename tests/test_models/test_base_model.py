"""Test module for the BaseModel class"""
from models.base_model import BaseModel, Base
import unittest
import datetime


class TestBaseModel(unittest.TestCase):
    """Test suit for the BaseModel class"""
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up an base model object for
        multiple testes
        """
        cls.bm = BaseModel()
    
    def test_base_subclass(self):
        """Test that base_model is a subclass
        of Declarative Base class from sqlalchemy
        """
        self.assertTrue(issubclass(BaseModel, Base))
    
    def test_id_attr(self):
        """Test that bm has id attr"""
        self.assertTrue(hasattr(self.bm, 'id'))
        self.assertTrue(type(self.bm.id) == str)
    
    def test_created_at_attr(self):
        """Test that bm has created_at attr"""
        self.assertTrue(hasattr(self.bm, 'created_at'))
        self.assertTrue(isinstance(self.bm.created_at, datetime.datetime))
    
    def test_updated_at_attr(self):
        """Test that bm has updated_at attr"""
        self.assertTrue(hasattr(self.bm, 'updated_at'))
        self.assertTrue(isinstance(self.bm.updated_at, datetime.datetime))
    
    def test_id_is_unique(self):
        """Test that object is unique"""
        bm2 = BaseModel()
        self.assertNotEqual(self.bm.id, bm2.id)
    
    def test_str_method(self):
        """Test that string representation of instance
        is return when obj passed in print() or str()
        """
        new_str = '{} ({}) {}'.format(
            self.bm.__class__.__name__,
            self.bm.id,
            self.bm.__dict__
        )
        self.assertEqual(new_str, str(self.bm))
    
    def test_to_dict_method(self):
        """Test the to_dict() method"""
        new_dict = self.bm.to_dict()
        self.assertTrue(isinstance(new_dict, dict))
        self.assertTrue('_sa_instance_state' not in new_dict)
        self.assertTrue(type(new_dict['created_at']) == str)
        self.assertTrue(type(new_dict['updated_at']) == str)
        self.assertTrue('password_hash' not in new_dict)

    
    @classmethod
    def tearDownClass(cls) -> None:
        """Deletes the base model object"""
        del cls.bm
