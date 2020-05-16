import unittest

from validation import validate_usr

class TestValidUsr(unittest.TestCase):
    def valid_test(self):
        self.assertEqual(validate_usr("vinayak",3),True)
    def too_short(self):
        self.assertEqual(validate_usr('eng',5),False)
    def invalid_char(self):
        self.assertEqual(validate_usr("invalid_user",1),False)
    def test_invalid_minlen(self):
        self.assertRaises(ValueError,validate_usr,"user",-1)
        
unittest.main()        



