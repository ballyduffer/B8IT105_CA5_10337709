from calculator import Calculator #import Calculator class from workings
import unittest   #import unit test to run self assertion tests to ensure exact value is calculated

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()   #assign Calculator() function to self.calc

	#Test add() function using self assert
    def test_calculator_add(self):
        self.assertEqual(9, self.calc.add([2,3,4])) #Even numbers
        self.assertEqual(-9, self.calc.add([-2,-3,-4])) #Odd numbers
        self.assertEqual(-1, self.calc.add([2,-3])) #Combination
        self.assertEqual(13, self.calc.add([5,-3,0,5,6])) #Combination, longer list, and zero
        self.assertEqual(ValueError, self.calc.add([5,'a',0,5,6])) #Value error when string entered

	#Test subtract() function using self assert
    def test_calculator_subtract(self):
        self.assertEqual(-5, self.calc.subtract([2,3,4])) #Postives
        self.assertEqual(5, self.calc.subtract([-2,-3,-4])) #Negatives
        self.assertEqual(5, self.calc.subtract([2,-3])) #Combination
        self.assertEqual(-3, self.calc.subtract([5,-3,0,5,6])) #Longer list including zero
        self.assertEqual(ValueError, self.calc.subtract([5,'a',0,5,6])) #Value error when string entered
        self.assertEqual(ValueError, self.calc.subtract(2)) #Value error when no list entered

	#Test multiply() function using self assert
    def test_calculator_multiply(self):
        self.assertEqual(24, self.calc.multiply([2,3,4])) #Positives
        self.assertEqual(-24, self.calc.multiply([-2,-3,-4])) #Negatives
        self.assertEqual(-6, self.calc.multiply([2,-3])) #Combination
        self.assertEqual(0, self.calc.multiply([5,-3,0,5,6])) #Zero
        self.assertEqual(ValueError, self.calc.subtract([5,'a',0,5,6])) #Value error when string entered

	#Test division() function using self assert
    def test_calculator_divide(self):
        self.assertEqual(2, self.calc.divide([40,10,2])) #Positives
        self.assertEqual(-2, self.calc.divide([-40,-10,-2])) #Negatives
        self.assertEqual(-0.6666666666666666, self.calc.divide([2,-3])) #Combination
        self.assertEqual(ValueError, self.calc.divide([5,-3,0,5,6])) #Value error when dividing by zero
        self.assertEqual(ValueError, self.calc.subtract([5,'a',0,5,6])) #Value error when string entered

	#Test square() function using self assert
    def test_calculator_square(self):
        self.assertEqual([4,9,16], self.calc.square([2,3,4])) #General test
        self.assertEqual([4,9,16], self.calc.square([-2,-3,-4])) #Negatives
        self.assertEqual([0.010000000000000002, 0.04000000000000001], self.calc.square([.1,.2])) #Floats
        self.assertEqual([25,9,0,25,36], self.calc.square([5,-3,0,5,6])) #Longer list including zero
        self.assertEqual(ValueError, self.calc.square([5,'a',0,5,6])) #Value error when string entered

	#Test square_root() function using self assert
    def test_calculator_square_root(self):
        self.assertEqual([2,3,4], self.calc.square_root([4,9,16])) #General test
        self.assertEqual(ValueError, self.calc.square_root([-2,-3,-4])) #Value error with negatives
        self.assertEqual([2,0], self.calc.square_root([4,0])) #Zero
        self.assertEqual(ValueError, self.calc.square_root([5,'a',0,5,6])) #Value error when string entered

	#Test tan() function using self assert
    def test_calculator_tan(self):
        self.assertEqual([1.1578212823495777, -0.45231565944180985, 0.3006322420239034], self.calc.tan([4,9,16])) #Postives
        self.assertEqual([2.185039863261519, 0.1425465430742778, -1.1578212823495777], self.calc.tan([-2,-3,-4])) #Negatives
        self.assertEqual([1.1578212823495777, 0.0], self.calc.tan([4,0])) #Zero
        self.assertEqual(ValueError, self.calc.tan([5,'a',0,5,6])) #Value error when string entered

	#Test cos() function using self assert
    def test_calculator_cos(self):
        self.assertEqual([-0.6536436208636119, -0.9111302618846769, -0.9576594803233847], self.calc.cos([4,9,16])) #Positives
        self.assertEqual([-0.4161468365471424, -0.9899924966004454, -0.6536436208636119], self.calc.cos([-2,-3,-4])) #Negatives
        self.assertEqual([-0.6536436208636119, 1.0], self.calc.cos([4,0])) #Zero
        self.assertEqual(ValueError, self.calc.cos([5,'a',0,5,6])) #Value error when string entered

	#Test sin() function using self assert
    def test_calculator_sin(self):
        self.assertEqual([-0.7568024953079282, 0.4121184852417566, -0.2879033166650653], self.calc.sin([4,9,16])) #Postives
        self.assertEqual([-0.9092974268256817, -0.1411200080598672, 0.7568024953079282], self.calc.sin([-2,-3,-4])) #Negatives
        self.assertEqual([-0.7568024953079282, 0.0], self.calc.sin([4,0])) #Zero
        self.assertEqual(ValueError, self.calc.sin([5,'a',0,5,6])) #Value error when string entered

	#Test odd() function using self assert
    def test_calculator_odd(self):
        self.assertEqual([3], self.calc.odd([2,3,4])) #Combination
        self.assertEqual([-3], self.calc.odd([-2,-3,-4])) #Combination with negatives
        self.assertEqual([1,1,3,7], self.calc.odd([0,1,1,3,7])) #Zero with list of negatives
        self.assertEqual([], self.calc.odd([2,4,6])) #All even
        self.assertEqual(ValueError, self.calc.subtract([5,'a',0,5,6])) #Value error when string entered

	#Test even() function using self assert
    def test_calculator_even(self):
        self.assertEqual([2,4], self.calc.even([2,3,4])) #Combination
        self.assertEqual([-2,-4], self.calc.even([-2,-3,-4])) #Combination with negatives
        self.assertEqual([0], self.calc.even([0,1,1,3,7])) #Zero with list of negatives
        self.assertEqual([], self.calc.even([1,3,5])) #All odd
        self.assertEqual(ValueError, self.calc.subtract([5,'a',0,5,6])) #Value error when string entered


if __name__ == '__main__':
    unittest.main()