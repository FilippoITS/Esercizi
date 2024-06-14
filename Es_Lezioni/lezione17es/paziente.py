from persona import Persona

class Paziente(Persona):

    def __init__(self, nome: str, cognome: str, id:str) -> None:
        super().__init__(nome, cognome)
        self.__id = id
    

    def setidCode(self, id:str) -> None:
        self.__id = id
    

    def getidCode(self) -> str:
        return self.__id
    

    def patientInfo(self) -> str:
        return f"Paziente: {self.get_name()}, {self.get_surname()} \nID: {self.__id}"
    
a = Paziente("Mario","Draghi","siaooa")
print(a.patientInfo())