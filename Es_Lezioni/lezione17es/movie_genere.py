from film import Film

class Azione(Film):

    def __init__(self, id: int, titolo: str) -> None:
        super().__init__(id, titolo)
        self.__genere:str = "Azione"
        self.__penale:float = 3

    def getGenere(self) -> str:
        return self.__genere

    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleritardo(self, giorni_di_ritardo:int) -> float:
        return giorni_di_ritardo * self.__penale


class Commedia(Film):

    def __init__(self, id: int, titolo: str) -> None:
        super().__init__(id, titolo)
        self.__genere:str = "Commedia"
        self.__penale:float = 2.50

    def getGenere(self) -> str:
        return self.__genere

    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleritardo(self, giorni_di_ritardo:int) -> float:
        return giorni_di_ritardo * self.__penale


class Drammatico(Film):

    def __init__(self, id: int, titolo: str) -> None:
        super().__init__(id, titolo)
        self.__genere:str = "Commedia"
        self.__penale:float = 2

    def getGenere(self) -> str:
        return self.__genere

    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleritardo(self, giorni_di_ritardo:int) -> float:
        return giorni_di_ritardo * self.__penale