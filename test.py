import unittest
import random

from s_cal import Expression


class Test(unittest.TestCase):

    def test_one_int(self):
        sample_test = Expression()
        
        # explicit checks
        self.assertEqual(sample_test.calculate('0'), 0)
        self.assertEqual(sample_test.calculate('1'), 1)
        self.assertEqual(sample_test.calculate('16'), 16)
        self.assertEqual(sample_test.calculate('32'), 32)
        self.assertEqual(sample_test.calculate('128'), 128)
        self.assertEqual(sample_test.calculate('256'), 256)

        # check 1,000 random values between 0 through 999999 
        for i in range(0, 1000):
            val = random.randrange(999999)
            self.assertEqual(sample_test.calculate(str(val)), val)

    def test_single_add(self):
        sample_test = Expression()
        
        # explicit checks
        self.assertEqual(sample_test.calculate('(add 1 1)'), 2)
        self.assertEqual(sample_test.calculate('(add 12 34)'), 46)

        # check 2 random values between 0 through 999999 (1,000 times)
        for i in range(0, 1000):
            a = random.randrange(999999)
            b = random.randrange(999999)
            self.assertEqual(sample_test.calculate('(add ' + str(a) + ' ' + str(b) + ')'), a + b)

    def test_single_multiply(self):
        sample_test = Expression()
        
        # explicit checks
        self.assertEqual(sample_test.calculate('(multiply 1 1)'), 1)
        self.assertEqual(sample_test.calculate('(multiply 12 34)'), 408)

        # check 2 random values between 0 through 999999 (1,000 times)
        for i in range(0, 1000):
            a = random.randrange(999999)
            b = random.randrange(999999)
            self.assertEqual(sample_test.calculate('(multiply ' + str(a) + ' ' + str(b) + ')'), a * b)

    def test_nested_functions(self):
        sample_test = Expression()
        
        # explicit tests
        # add only
        self.assertEqual(sample_test.calculate('(add 0 (add 3 4))'), 7)
        self.assertEqual(sample_test.calculate('(add 3 (add (add 3 3) 3))'), 12)
        
        # multiply only
        self.assertEqual(sample_test.calculate('(multiply 0 (multiply 3 4))'), 0)
        self.assertEqual(sample_test.calculate('(multiply 2 (multiply 3 4))'), 24)
        self.assertEqual(sample_test.calculate('(multiply 3 (multiply (multiply 3 3) 3))'), 81)

        #mix
        self.assertEqual(sample_test.calculate('(add 1 (multiply 2 3))'), 7)
        self.assertEqual(sample_test.calculate('(multiply 2 (add (multiply 2 3) 8))'), 28)
        
        #more complex
        self.assertEqual(sample_test.calculate('(add 1 2 3 4 (multiply 2 3 5))'), 40)


if __name__ == '__main__':
    random.seed()
    unittest.main()