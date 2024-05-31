"""Exercise 1: Creating an Abstract Class with Abstract Methods
Create an abstract class Shape with an abstract method area and another abstract method perimeter. 
Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods."""
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self, ):
        pass


class Cricle(Shape):
    
    def area(self, pi:float, r:float) -> float:
        return pi * r**2


class Rectangle(Shape):

    def area(self, b:float, h:float) -> float:
        return b*h


"""Exercise 2: Implementing Static Methods
Create a class MathOperations with a static method add that takes two numbers and returns their sum, 
and another static method multiply that takes two numbers and returns their product."""
class MathOperations:

    @staticmethod
    def sum(x:int, y:int) -> int:
        return x + y
    
    def multiply(x:int, y:int) -> int:
        return x * y
