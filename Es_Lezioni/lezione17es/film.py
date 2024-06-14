class Film:

    def __init__(self, id:int, titolo:str) -> None:
        self.id = id
        self.titolo = titolo
    

    def setID(self, id:int) -> None:
        self.id = id
    

    def setTitle(self, title:str) -> None:
        self.titolo = title

    
    def getID(self) -> int:
        return self.id


    def getTitle(self) -> str:
        return self.titolo
    

    def isEquale(self, altro_film) -> bool:
        if self.id == altro_film.id:
            return True
        else:
            return False