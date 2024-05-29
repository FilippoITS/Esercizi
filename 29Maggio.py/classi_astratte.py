from abc import ABC, abstractmethod

class abcanimal(ABC):
    
    @abstractmethod
    def verso(self):
        pass


class Cane(abcanimal):
    def __init__(self, nome:str) -> None:
        self.nome = nome
    
    def verso(self):
        print("BAU!")


class Gatto(abcanimal):
    def __init__(self, nome:str) -> None:
        self.nome = nome
    
    def verso(self):
        print("MIAOMIAO!")


class Coccodrillo(abcanimal):
    def __init__(self, nome:str) -> None:
        self.nome = nome
    
    def verso(self):
        print("VERSO DEL COCCODRILLO!")



doggo = Cane("arciduca Giovanni")
gattone = Gatto("carmen")
coccodr = Coccodrillo("Stellino")


doggo.verso()
gattone.verso()
coccodr.verso()




i:int = 0
assert i == 0, f"The value must be equal to 0 instaed of {i}" #assert da errore solo se falsa



