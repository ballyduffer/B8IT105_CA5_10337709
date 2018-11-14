
import math #brings in math functionality 
import functools #required for reduce function

class Calculator(object):

    #Adding function: Takes numbers as input and adds the contents.
    #Uses lambda & reduce.
    def add(self,numbers):
      try:
        return functools.reduce(lambda a,b:a+b,numbers)
      except:
          return ValueError

    #Subtract function: Takes numbers as input and subtracts the contents.
    #Uses lambda & reduce.
    def subtract(self,numbers):
      try:
        return functools.reduce(lambda a,b:a-b,numbers)
      except:
          return ValueError

    #Multiply function: Takes numbers as input and multiplies the contents.
    #Uses lambda & reduce.
    def multiply(self,numbers):
      try:
        return functools.reduce(lambda a,b:a*b,numbers)
      except:
          return ValueError

    #Divide function: Takes numbers as input and multiplies the contents.
    #Uses lambda & reduce.
    def divide(self,numbers):
      try:
        return functools.reduce(lambda a,b:a/b,numbers)
      except:
          return ValueError

    #Squared function: Takes numbers as input and squares each individual number.
    #Uses list comprehension.
    def square(self,numbers):
      try:
        return [a**2 for a in numbers]
      except:
          return ValueError

    #Square root function: Takes numbers as input and gets the square root of each individual number.
    #Uses list comprehension.
    def square_root(self,numbers):
      try:
        return [math.sqrt(a) for a in numbers]
      except:
          return ValueError

    #Tan function: Takes numbers as input and gets the tan of each individual number.
    #Uses lambda & map.
    def tan(self,numbers):
      try:
        return list(map(lambda a:math.tan(a),numbers))
      except:
          return ValueError

    #Sin function: Takes numbers as input and gets the tan of each individual number.
    #Uses lambda & map.
    def sin(self,numbers):
      try:
        return list(map(lambda a:math.sin(a),numbers))
      except:
          return ValueError

    #Cos function: Takes numbers as input and gets the tan of each individual number.
    #Uses lambda & map.
    def cos(self,numbers):
      try:
        return list(map(lambda a:math.cos(a),numbers))
      except:
          return ValueError

    #Odd Numbers: Takes numbers as input and returns all the odd numbers.
    #Uses lambda & filter.
    def odd(self,numbers):
      try:
        return list(filter(lambda a: a%2,numbers))
      except:
          return ValueError

    #Even Numbers: Takes numbers as input and returns all the even numbers.
    #Uses lambda & filter. 
    def even(self,numbers):
      try:
        return list(filter(lambda a: a%2 == 0,numbers))
      except:
          return ValueError

#Simple Tests
#calc = Calculator()
#print(calc.add([1,2,35,12]))
#print(calc.subtract([10,2]))
#print(calc.multiply([2,2,3]))
#print(calc.divide([20,5,3]))
#print(calc.square_root([2,4,16]))
#print(calc.square([2,4,16]))
#print(calc.tan(2))
#print(calc.sin([2,4,16]))
#print(calc.cos([2,4,16]))
#print(calc.odd([1,2,3]))
#print(calc.even([0,'16',1,1,1,3]))


