import unittest
from My_Library.Library_Opera.Data_ import *

class TestData(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.data = Data()
        
    @classmethod
    def tearDownClass(self):
        print('successful')
        
    def test_get(self):
        self.assertEqual(self.data.get_person_name('yuki'),'cyx')
        self.assertEqual(self.data.get_person_info_num('stu'),["cc",10])
        self.assertEqual(self.data.get_book_info('1'),-1)
        self.assertEqual(self.data.get_book_borrow_info('1492041130'),[1, "stu"])
        self.assertEqual(self.data.get_book_info_from_pos('position2')[0],'1492041130')
        
    def test_check(self):
        self.assertEqual(self.data.check_cate('yuki'),'admin')
        self.assertEqual(self.data.check_user('aaaaaa'),-1)
        self.assertEqual(self.data.check_book('1492041130'),1)
        self.assertEqual(self.data.check_user_pass('yuki','test'),1)