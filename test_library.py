import unittest
from My_Library.Library_Opera.Library_ import *
class TestLibrary(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.lib = Library()
        
    @classmethod
    def tearDownClass(self):
        print('successful')

    def test_sign(self):
        self.assertEqual(self.lib.sign_in_test('q',''),'quit')
        self.assertEqual(self.lib.sign_in_test('a','a'),"Please check your username and password!")
        self.assertEqual(self.lib.sign_in_test('yuki','test'),'admin')
        self.assertEqual(self.lib.sign_in_test('stu','123'),'user')
    
    def test_register(self):
        self.assertEqual(self.lib.register_test('q'),'quit')
        self.assertEqual(self.lib.register_test('yuki'),"The username is existed, please choose another one!")
        self.assertEqual(self.lib.register_test('test_name1'),'user quit')
        self.assertEqual(self.lib.register_test('test_name2'),'user centre quit')