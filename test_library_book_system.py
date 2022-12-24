import unittest

from My_Library.Library_Base.Library_Book_System import *

class TestLibrary_Book_System(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.b_a = Book_admin()
        self.b_u = Book_user()
        
    @classmethod
    def tearDownClass(self):
        print('successful')
        
    def test_book_user(self):
        self.assertEqual(self.b_u.search_position(),-1)
        self.assertEqual(self.b_u.borrow_book_test('stu','1408845687'),1)
        self.assertEqual(self.b_u.return_book_test('stu','test'),-1)
        self.assertEqual(self.b_u.number_book_log('stu_test'),0)
        
    def test_book_admin(self):
        self.assertEqual(self.b_a.input_book(),None)
        self.assertEqual(self.b_a.borrow_book_log_test('1492041130','stu'),-1)
        self.assertEqual(self.b_a.return_book_log_test('test'),-1)
        self.assertEqual(self.b_a.borrow_book_info(),None)