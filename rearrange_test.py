from rearrange_name import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        test_case = "Venkatesh,Vinayak"
        expected  = "Vinayak Venkatesh"
        self.assertEqual(rearrange_name(test_case),expected)
    def test_empty(self):
        test_case =""
        expected =""
        self.assertEqual(rearrange_name(test_case),expected)
    def test_double(self):
        test_case="Hopper,Grace M."
        expected="Grace M. Hopper"
        self.assertEqual(rearrange_name(test_case),expected)
    def test_one_name(self):
        test_case="Vinayak"
        expected="Vinayak"
        self.assertEqual(rearrange_name(test_case),expected)
unittest.main()    