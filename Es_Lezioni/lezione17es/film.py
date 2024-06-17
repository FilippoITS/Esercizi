class Film:

    def __init__(self, id:int, titolo:str) -> None:
        self.__id = id
        self.__titolo = titolo
    

    def setID(self, id:int) -> None:
        self.__id = id
    

    def setTitle(self, title:str) -> None:
        self.__titolo = title

    
    def getID(self) -> int:
        return self.__id


    def getTitle(self) -> str:
        return self.__titolo
    

    def isEqual(self, altro_film:"Film") -> bool:
        if self.__id == altro_film.__id:
            return True
        else:
            return False
        

a = Film(12, "Mario")
b = Film(12, "Paolo")

print(a.isEqual(b))