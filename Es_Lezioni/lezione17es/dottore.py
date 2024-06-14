from persona import Persona

class Dottore(Persona):

    def __init__(self, nome: str, cognome: str, specializzazione: str, parcella: float) -> None:
        super().__init__(nome, cognome)
        self.__specializzazione:str = specializzazione
        self.__parcella:float = parcella
        

        if type(self.__parcella) != float:
            self.__parcella = None
            print("La parcella non era un tipo float")
        
        if type(self.__specializzazione) != str:
            self.__specializzazione = None
            print("La specializzazione messa non era una stringa")


    def setSpecialization(self, specializzazione:str) -> str:
        if type(specializzazione) == str:
            self.__specializzazione = specializzazione
        else:
            self.__specializzazione = None
            print( f"Il valore di {specializzazione} non era una stringa")


    def setparcel(self, parcella:float) -> str:
        if type(parcella) == float:
            self.__parcella = parcella
        else:
            self.__parcella = None
            print( f"Il valore di {parcella} non è un tipo float")
    

    def getParcel(self) -> str:
        return self.__parcella
    

    def getSpecialization(self) -> str:
        return self.__specializzazione
    

    def isAValidDoctor(self) -> str:
        if self.get_age() > 30:
            print(f"Il dottore {self.get_name()}, {self.get_surname()} è valido")
            return True
        else:
            print(f"Il dottore {self.get_name()}, {self.get_surname()} non è valido")
            return False


    def greetDoctor(self) -> str:
        
        return self.greet() + f" ,Sono un medico{self.__specializzazione}"


a = Dottore("MArio","Giorgini","PazzoVero",123.3)
print(a.getSpecialization())
print(a.greetDoctor())
a.setAge(31)
print(a.get_age())
print(a.isAValidDoctor())
