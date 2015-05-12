from arith import * #import everything from arith
#from arith import add, mul, divide : it will import the corresponding functions
import unittest 


class TestArith(unittest.TestCase):

    def test_add(self):
        self.assertEqual(4, add(2, 2))
        
    def test_mul(self):
        self.assertEqual(4, mul(2, 2))
        self.assertEqual(6, mul(3, 2))

    def test_divide(self):
        self.assertEqual(1, divide(2, 2))
        self.assertEqual(50, divide(100, 2))
        self.assertEqual(4, divide(100, 25))
        self.assertRaises(AssertionError, divide, 10, 0) #it assert the error case. 
unittest.main()

