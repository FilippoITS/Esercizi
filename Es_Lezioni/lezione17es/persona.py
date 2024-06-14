class Persona:

    def __init__(self, nome:str, cognome:str) -> None:
        self.__nome:str = nome 
        self.__cognome:str = cognome
        
        if type(self.__nome) != str:
            self.__nome = None
            print("Il nome non è una stringa")
        
        if type(self.__cognome) != str:
            self.__cognome = None
            print("Il cognome non è un stringa")
        
        if type(self.__nome) == str and type(self.__cognome) == str:
            self.__età = 0
            return 
        
        if type(self.__nome) or type(self.__cognome) == None:
            self.__età = None
        
        
    

    def setName(self, name:str) -> None:
        if type(name) != str:
            return f"il nome {name} non è una stringa quindi non verrà cambiato"

        else:
            self.__nome = name
            print("Il nome è stato cambiato")
    
    
    def setSurname(self, surname:str) -> None:
        if type(surname) != str:
            return f"il nome {surname} non è una stringa quindi non verrà cambiato"

        else:
            self.__nome = surname
            print("Il nome è stato cambiato")

    
    def setAge(self, age:int) -> None:
        if type(age) != int:
            return f"L'età {age} non è un intero quindi non  verrà aggiunta"
        else:
            self.__età = age
            return self.__età
        
    
    def get_name(self) -> str:
        return self.__nome
    

    def get_surname(self) -> str:
        return self.__cognome
    

    def get_age(self) -> str:
        return self.__età


    def greet(self) -> str:
        return f"Ciao sono {self.__nome},{self.__cognome} e ho {self.__età} anni"



a = Persona("fafma" ,12)
print(a.get_name())
print(a.get_surname())
print(a.get_age())

