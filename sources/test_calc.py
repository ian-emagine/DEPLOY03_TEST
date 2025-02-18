import unittest
import calc

class TestCalc(unittest.TestCase):
    """
    Test the add function from the calc library
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = calc.add2(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = calc.add2('10.5', 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        """
        Test the addition of two strings returns the two strings as one
        concatenated string
        """
        result = calc.add2('abc', 'def')
        self.assertEqual(result, 'abcdef')

    def test_add_string_and_integer(self):
        """
        Test the addition of a string and an integer returns them as one
        concatenated string (in which the integer is converted to a string)
        """
        result = calc.add2('abc', 3)
        self.assertEqual(result, 'abc3')

    def test_add_string_and_number(self):
        """
        Test the addition of a string and a float returns them as one
        concatenated string (in which the float is converted to a string)
        """
        result = calc.add2('abc', '5.5')
        self.assertEqual(result, 'abc5.5')

    """
    Test the multiply function from the calc library
    """

    def test_multiply_integers(self):
        """
        Test that the multiplication of two integers returns the correct total
        """
        result = calc.multi2(1, 2)
        self.assertEqual(result, 2)

    def test_multiply_floats(self):
        """
        Test that the multiplication of two floats returns the correct result
        """
        result = calc.multi2('10.5', 2)
        self.assertEqual(result, 21)

    def test_multiply_strings(self):
        """
        Test the multiplication of two strings returns the two strings as one
        concatenated string
        """
        result = calc.multi2('abc', 'def')
        self.assertEqual(result, 'Can not multiply two strings nor a float and a string')

    def test_multiply_string_and_integer(self):
        """
        Test the multiplicationv of a string and an integer returns them as one
        concatenated string (in which the integer is converted to a string)
        """
        result = calc.multi2('abc', 3)
        self.assertEqual(result, 'abcabcabc')

    def test_multiply_string_and_float(self):
        """
        Test the multiplication of a string and a float returns them as one
        concatenated string (in which the float is converted to a string)
        """
        result = calc.multi2('abc', '5.5')
        self.assertEqual(result, 'Can not multiply two strings nor a float and a string')

        
if __name__ == '__main__':
    unittest.main()
