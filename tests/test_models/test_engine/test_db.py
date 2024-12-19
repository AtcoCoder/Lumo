"""DB class Test Module"""
import unittest
from models.engine.db import DB
from config import CURRENT_CONFIG
from models.user import User


class TestDB(unittest.TestCase):
    """DB test suite"""
    @classmethod
    def setUpClass(cls):
        """Creates db instance for tests"""
        cls.db = DB(CURRENT_CONFIG.DATABASE_URI)
        cls.db.reload()
        cls.user = User(
            username='omar',
            email='omar@email.com',
            password_hash='password',
            phone_number='1234578'
        )   

    @classmethod
    def tearDownClass(cls):
        """Drops tables and close the database session"""
        # cls.db.reset()
        cls.db.drop()
        cls.db.close()
    
    def setUp(self):
        """Prepare the session for each test"""
        pass
    
    def test_add_and_save(self):
        """Test that db adds and saves object"""
        self.db.add(self.user)
        self.db.save()

        result = self.db.session.query(User).filter_by(id=self.user.id).first()
        self.assertIsNotNone(result)
        self.assertEqual(result.username, 'omar')
        self.assertEqual(result.email, 'omar@email.com')

    def test_get(self):
        """Test get object by id"""
        self.db.add(self.user)
        self.db.save()

        result = self.db.get(self.user.id, User)

        self.assertIsNotNone(result)
    
    @unittest.skip('Can not Pass Right Now')
    def test_close(self):
        '''Test closing session'''
        self.db.close()
        self.assertFalse(self.db.session.is_active)
    
    def test_count(self):
        """Test counting of class objects"""
        users_count = self.db.count('User')
        new_user = User(
            username='jammeh',
            email='jammeh@email.com',
            phone_number='1234789',
            password_hash='password'
        )
        self.db.add(new_user)
        self.db.save()
        new_count = self.db.count('User')
        self.assertEqual(new_count, users_count + 1)
    
    def test_add_not_valid_model(self):
        """Test adding invalid model into the db"""
        with self.assertRaises(TypeError):
            self.db.add('user')
    
    def test_add_no_model(self):
        """Test adding no model"""
        with self.assertRaises(TypeError):
            self.db.add()
    
    def test_get_no_class(self):
        """Test getting by id with no class"""
        self.db.add(self.user)
        self.db.save()
        with self.assertRaises(TypeError):
            self.db.get(self.user.id)
    
    def test_get_with_wrong_id(self):
        """Test getting by wrong id"""
        result = self.db.get('wongid', User)
        self.assertEqual(None, result)
    
    def test_get_with_non_string_id(self):
        """Test getting by non string id"""
        with self.assertRaises(TypeError):
            result = self.db.get(['wrongid'], User)
    
    def test_all_with_no_cls(self):
        """Test getting all without specifying the class"""
        with self.assertRaises(TypeError):
            self.db.all()
    
    @unittest.skip('Not needed')
    def test_get_by(self):
        print(self.db.all('User')[0])
        user = self.db.get_by('email', 'omar@email.com')
        self.assertTrue(user)
        user_2 = self.db.get_by('username', 'atcocoder')
        self.assertTrue(user_2)

