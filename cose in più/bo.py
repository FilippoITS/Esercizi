import unittest

class Calculation():

    def __init__(self, num1, num2)-> None:
        self.num1 = num1
        self.num2 = num2
    
    def get_Sum(self):
        return self.num1 + self.num2
    
    def get_difference(self):
        return self.num1 - self.num2

    def get_product(self):
        return self.num1 * self.num2

    def get_quotient(self):
        return self.num1 / self.num2
            