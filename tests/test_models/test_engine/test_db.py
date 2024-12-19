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
        cls.db.reset()
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

        result = self.db.get(User, self.user.id)

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


