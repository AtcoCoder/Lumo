from models.user import User
from models.base_model import BaseModel, Base
import unittest

EMAIL = 'orms@email.com'
USERNAME = 'atcocoder'
PHONE = '12345678'
WHATSAPP = '12345678'
PASSWORD = 'secret'


class TestUser(unittest.TestCase):
    """Test suite for the User class"""
    @classmethod
    def setUpClass(cls):
        """Creates user instance for multiple tests"""
        cls.user = User(
            email=EMAIL,
            username=USERNAME,
            phone_number=PHONE,
            password_hash=PASSWORD
        )
    def test_create_user(self):
        """create user instance test case"""
        self.assertTrue(isinstance(self.user, User))
    
    def test_user_superclass(self):
        """test user superclass"""
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(issubclass(User, Base))
    
    def test_id_attr(self):
        """Test that user has id attribute"""
        user = User(
            email=EMAIL,
            username=USERNAME,
            phone_number=PHONE,
            password_hash=PASSWORD
        )
        self.assertTrue(hasattr(user, 'id'))
    
    def test_username_attr(self):
        """Test that user has username attribute"""
        user = User(
            email=EMAIL,
            username=USERNAME,
            phone_number=PHONE,
            password_hash=PASSWORD
        )
        self.assertTrue(hasattr(user, 'username'))
    
    def test_email_attr(
            self):
        """Test that user has email attr"""
        user = User(
            email=EMAIL,
            username=USERNAME,
            phone_number=PHONE,
            password_hash=PASSWORD
        )
        self.assertTrue(hasattr(user, 'email'))

    def test_password_attr(self):
        """Test that user has password attr"""
        user = User(
            email=EMAIL,
            username=USERNAME,
            phone_number=PHONE,
            password_hash=PASSWORD
        )
        self.assertFalse(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'password_hash'))
    
    def test_phone_number_attr(self):
        """Test that user has phone_number attr"""
        user = User(
            email=EMAIL,
            username=USERNAME,
            phone_number=PHONE,
            password_hash=PASSWORD
        )
        self.assertTrue(hasattr(user, 'phone_number'))
    
    def test_created_at_attr(self):
        """Test that user has created_at attr"""
        user = User(
            email=EMAIL,
            username=USERNAME,
            phone_number=PHONE,
            password_hash=PASSWORD
        )
        self.assertTrue(hasattr(user, 'created_at'))
    
    def test_updated_at_attr(self):
        """Test that user has updated_at attr"""
        user = User(
            email=EMAIL,
            username=USERNAME,
            phone_number=PHONE,
            password_hash=PASSWORD
        )
        self.assertTrue(hasattr(user, 'updated_at'))

    def test_to_dict_method(self):
        """Test that to_dict() creates a 
        dictionary with key/values pairs
        of the object.
        """
        user = User(
            email=EMAIL,
            username=USERNAME,
            phone_number=PHONE,
            password_hash=PASSWORD
        )
        user.email = 'omar@email.com'

        new_dict = user.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attr in user.__dict__:
            if attr != '_sa_instance_state' and attr != 'password_hash':
                self.assertTrue(attr in new_dict)
        self.assertTrue('__class__' in new_dict)
    
    def test_update_user(self):
        """Test that update() method
        updates correctly
        """
        user = User(
            email=EMAIL,
            username=USERNAME,
            phone_number=PHONE,
            password_hash=PASSWORD
        )
        user.email = 'unchanged@email.com'
        user.username = 'Atcocder'
        updated_time = user.updated_at
        user.update(email='changed@email', username='AtcoCoder')
        self.assertNotEqual(user.email, 'unchanged@email.com')
        self.assertNotEqual(user.username, 'Atcocder')
        self.assertNotEqual(updated_time, user.updated_at)

    def test_creating_user_with_kwargs(self):
        """Test that user can be create with
        key value arguments
        """

        user = User(
            email=EMAIL,
            username=USERNAME,
            phone_number=PHONE,
            whatsapp=WHATSAPP,
            password_hash=PASSWORD
       )

        self.assertEqual(user.email, EMAIL)
        self.assertEqual(user.username, USERNAME)
        self.assertEqual(user.phone_number, PHONE)
        self.assertEqual(user.whatsapp, WHATSAPP)
    
    def test_password_attr_missing(self):
        """Test that password attr is present
        when creating user
        """
        with self.assertRaises(AttributeError):
            User()
    
    def test_missing_email(self):
        """Test that user is created with email
        """
        with self.assertRaises(AttributeError):
            User(
                password_hash=PASSWORD
            )
    
    def test_missing_username(self):
        """Test that user is created with username
        """
        with self.assertRaises(AttributeError):
            User(
                password_hash=PASSWORD,
                email=EMAIL
            )
    
    def test_phone_number(self):
        """Test that user is created with
        phone number
        """
        with self.assertRaises(AttributeError):
            User(
                password_hash=PASSWORD,
                email=EMAIL,
                username=USERNAME
            )

    def test_email_is_str(self):
        """Test that email is string"""
        with self.assertRaises(ValueError):
            User(
                password_hash=PASSWORD,
                email=10,
                username=USERNAME,
                phone_number=PHONE
            )
    
    def test_username_is_str(self):
        """Test that username is string"""
        with self.assertRaises(ValueError):
            User(
                password_hash=PASSWORD,
                email=EMAIL,
                username=1010,
                phone_number=PHONE
            )

    def test_password_is_str(self):
        """Test that password is string"""
        with self.assertRaises(ValueError): 
            User(
                password_hash=PASSWORD,
                email=EMAIL,
                username=USERNAME,
                phone_number=1234
            )
    
    def test_whatsapp_is_str(self):
        """Test that whatsapp number is string"""
        with self.assertRaises(ValueError):
            User(
                password_hash=PASSWORD,
                email=EMAIL,
                username=USERNAME,
                phone_number=PHONE,
                whatsapp=123458
            )

    # def test_email_update(self):
    #     """Test that input is validated at
    #     email update
    #     """
    #     with self.assertRaises(ValueError):
    #         self.user.email = 10
    
    # def test_username_update(self):
    #     """Test that input is validated for
    #     username update
    #     """
    #     with self.assertRaises(ValueError):
    #         self.user.username = None
    
    # def test_phone_number_update(self):
    #     """Test that input is validated for
    #     phone number update
    #     """
    #     with self.assertRaises(ValueError):
    #         self.user.phone_number = [0]
    
    # def test_password_hash_update(self):
    #     """Test that input is validated for
    #     password_hash update
    #     """
    #     with self.assertRaises(ValueError):
    #         self.user.password_hash = ()
    
    # def test_whatsapp_update(self):
    #     """Test that input is validated for
    #     whatsapp update
    #     """
    #     with self.assertRaises(ValueError):
    #         self.user.whatsapp = 10.10
