from models.user import User
from models.base_model import BaseModel, Base
import unittest


class TestUser(unittest.TestCase):
    """Test suite for the User class"""
    def test_create_user(self):
        """create user instance test case"""
        user = User()
        self.assertTrue(isinstance(user, User))
    
    def test_user_superclass(self):
        """test user superclass"""
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(issubclass(User, Base))
    
    def test_id_attr(self):
        """Test that user has id attribute"""
        user = User()
        self.assertTrue(hasattr(user, 'id'))
    
    def test_username_attr(self):
        """Test that user has username attribute"""
        user = User()
        self.assertTrue(hasattr(user, 'username'))
    
    def test_email_attr(
            self):
        """Test that user has email attr"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))

    def test_password_attr(self):
        """Test that user has password attr"""
        user = User()
        self.assertFalse(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'password_hash'))
    
    def test_phone_number_attr(self):
        """Test that user has phone_number attr"""
        user = User()
        self.assertTrue(hasattr(user, 'phone_number'))
    
    def test_created_at_attr(self):
        """Test that user has created_at attr"""
        user = User()
        self.assertTrue(hasattr(user, 'created_at'))
    
    def test_updated_at_attr(self):
        """Test that user has updated_at attr"""
        user = User()
        self.assertTrue(hasattr(user, 'updated_at'))

    def test_to_dict_method(self):
        """Test that to_dict() creates a 
        dictionary with key/values pairs
        of the object.
        """
        user = User()
        user.email = 'omar@email.com'

        new_dict = user.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attr in user.__dict__:
            if attr != '_sa_instance_state':
                self.assertTrue(attr in new_dict)
        self.assertTrue('__class__' in new_dict)
    
    def test_update_user(self):
        """Test that update() method
        updates correctly
        """
        user = User()
        user.email = 'unchanged@email.com'
        user.username = 'Atcocder'
        updated_time = user.updated_at
        user.update(email='changed@email', username='AtcoCoder')
        self.assertNotEqual(user.email, 'unchanged@email.com')
        self.assertNotEqual(user.username, 'Atcocder')
        self.assertNotEqual(updated_time, user.updated_at)

