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
            



def isPalindrome( x: int) -> bool:
        
        counter = 0
        s_x = str(x)
        s_x_rev = s_x[::-1]
        for i in range(len(s_x)):
            if s_x[i] == s_x_rev[i]:
                counter += 1
        return counter

        

x = 121
print(isPalindrome(x))