from abc import abstractmethod
from abc import ABC

class Forma(ABC):

    def __init__(self, base:int, lato:int) -> None:
        self.base:int = base
        self.lato: int = lato
    

    @abstractmethod
    def area(self):
        pass
    
    def render(self):
        pass

