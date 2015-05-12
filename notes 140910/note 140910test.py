import unittest #it's a test
import arith #introduce the code file

class TestArith(unittest.TestCase):

    def test_add(self):
        self.assertEqual(4, arith.add(2, 2)) #we need to specify arith.add, not add
        
    def test_mul(self):
        self.assertEqual(4, arith.mul(2, 2))
        self.assertEqual(6, arith.mul(3, 2))
        self.assertEqual(10, arith.mul(2, 5))
        self.assertEqual(25, arith.mul(5, 5))
        
unittest.main()

