from abc import ABC
from abc import abstractmethod

from person import Student

class CourseAB(ABC):

    def __init__(self, name:str) -> None:
        super().__init__(self)
        self.name = self
    
    @abstractmethod
    def register_student(self, student: Student):
        pass