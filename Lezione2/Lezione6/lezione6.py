class Person:
    def __init__(self, name, age, height, wheight):
        self.name = name
        self.age = age
        self.height = height
        self.wheight = wheight
        self.hobby = []
    
    def __str__(self) -> str: #deve essere rigorosamente ua stringa
        return f"{self.name}, {self.age}, {self.height}, {self.wheight}"

    def torna_età(self) -> int:
        return f"l'età è {self.age}"
    
    def bulk_set_hobby(self,new_obbies:list):
        self.hobby += new_obbies

    def set_hobby(self, hobby:str) -> str:
        self.hobby.append(hobby)
    
    def remove_hobby(self, oldhobby:str):
        self.hobby.remove(oldhobby)

    
alice = Person("Alice W.", 45, "123 cm" , 78)
bob = Person("Bob M.", 36, "124cm", 85)
patrick = Person("Patrick.L", 27, "3255cm", 5325)
gimmy = Person("Gimmy.D", 64, "252cm", 532)
folpi = Person("Filippo.S", 48, "14151cm", 144)

persons:list = [alice,bob,patrick,gimmy,folpi]

print(bob.age)

if bob.age > alice.age:
    print(f"Il più grande è {bob.name}")
else:
    print(f"il più grande è {alice.age}")


min_age: int = float('inf')
index_min_age:int = 0
for i in range(len(persons)):
    if persons[i].age < min_age:
        min_age = persons[i].age
        index_min_age = i
persona = persons[index_min_age]

print(f"Il nome della perone più giovane è {persona.name} con età {persona.age}, aletezz = {persona.height}, peso = {persona.wheight}")

print(f"la persona più giovane è : {persona}")

print(alice.torna_età()) #ho creato questa funzione nella classe per farmi tornare solo l'età

alice.set_hobby("rugby")
print(f"l'hobby di alice è {alice.hobby}")          
alice.set_hobby("MARTE")
print(f"Gli hobby di alice sono : {alice.hobby}")
alice.remove_hobby("MARTE")
print(f"Ora gli hobby sono: {alice.hobby}")
alice.bulk_set_hobby(["violino","pianoforte","dj"])
print(alice.hobby)

###############################################################################################

class Student:
    def __init__(self, name, studyprogram,
                       age, gender) -> None:
        self.name = name
        self.studyprogram = studyprogram
        self.age = age
        self.gender = gender
    
    def print_info(self) -> str:    
        return f"Nome= {self.name}, Percorso di studi= {self.studyprogram}, Età= {self.age}, Genere= {self.gender}"

Io = Student("Filippo.G", "Its", 20, "M")
Alberto = Student("Alberto.B", "Its", 32, "M")
MariaPaola = Student("MariaPaola.B", "Its", "Bo", "F")
print(f"{Io.print_info()}\n{Alberto.print_info()} \n{MariaPaola.print_info()}")

###############################################################################################

class Student1:
    
    student_grades:list[int] = []
    
    def __init__(self, name, ) -> None:
        self.name = name      
        self.my_grades:list = []
    
    def add_grades(self,grades):
        self.my_grades.append(grades)
        self.student_grades.append(grades)
    
    def print_grade(self):
        print(f"Il mio voto è {self.student_grades}")
    
    classmethod
    def average_grades(cls) -> float:
        avg = sum(cls.student_grades) / len(cls.average_grades)
        return avg    
    

me = Student1("Filippo")
tu = Student1("Paolo")
print(Student1.student_grades)

me.add_grades(8)
me.add_grades(2)
me.add_grades(9)

Student1.print_grade(me)

###############################################################################################
print("################################")
class Animal:
    
    def __init__(self, colore, zampe) -> None:
        self.colore = colore
        self.zampe = zampe

    def print_info(self):
        print(f"{self.colore},{self.zampe}")

    def change_leg(self,nuovezampe:int):
        self.zampe = nuovezampe

    
    def get_legs(self):
        print(f"L'animale in questione ha {self.zampe} zampe")

cane = Animal("Blu",2)
cane.get_legs()
cane.change_leg(6)
cane.get_legs()

topo = Animal("verde",4)
topo.get_legs()
topo.change_leg(8)
topo.get_legs()

cane.print_info()
topo.print_info()

###############################################################################################
print("################################")
class Food:

    def ciboo(self, name:str, price:str, description:str) -> None:
        pass