import unittest
from test_data import TestData
from test_library import TestLibrary
from test_library_book_system import TestLibrary_Book_System
from test_library_person import TestLibrary_Person

test_cases = (TestData,TestLibrary,TestLibrary_Book_System,TestLibrary_Person)

def test_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestData))
    suite.addTest(unittest.makeSuite(TestLibrary))
    suite.addTest(unittest.makeSuite(TestLibrary_Book_System))
    suite.addTest(unittest.makeSuite(TestLibrary_Person))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
test_suite()