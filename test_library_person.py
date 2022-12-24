import unittest

from My_Library.Library_Base.Library_Person import *

class TestLibrary_Person(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.admin = Admin('yuki')
        self.user = User('stu')
        
    @classmethod
    def tearDownClass(self):
        print('successful')
        
    def test_admin(self):
        print('1 1 0 0')
        self.assertEqual(self.admin.menu(),"admin quit")
        print('1 0')
        self.assertEqual(self.admin.menu(),"admin user mana quit")
        print('2 1 0')
        self.assertEqual(self.admin.menu(),"admin quit")
        print('2 2 0')
        self.assertEqual(self.admin.menu(),"admin quit")
        print('2 3 0')
        self.assertEqual(self.admin.menu(),"admin quit")
        print('2 0')
        self.assertEqual(self.admin.menu(),"admin book mana quit")
        print('3 0')
        self.assertEqual(self.admin.menu(),"admin borrow mana quit")
        print('0')
        self.assertEqual(self.admin.menu(),"admin quit")
        self.assertEqual(self.admin.user_info(),'user_info')
        self.assertEqual(self.admin.edit_user_info(),'edit quit')
        self.assertEqual(self.admin.cate,'admin')
        
    def test_user(self):
        print('0')
        self.assertEqual(self.user.menu(),'user quit')
        print('1 1 0')
        self.assertEqual(self.user.menu(),"user quit")
        print('1 0')
        self.assertEqual(self.user.menu(),"user centre quit")
        print('2 0')
        self.assertEqual(self.user.menu(),"user b_r_center quit")
        print('3 0')
        self.assertEqual(self.user.menu(),"user quit")
        self.assertEqual(self.user.my_info(),'user info')
        self.assertEqual(self.user.change_username_test("stu"),'This username is already in the library!')
        self.assertEqual(self.user.change_username_test("stu1"),'change_succ')
