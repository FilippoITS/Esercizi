class Person:

    def __init__(self, cf: str, name:str, surname:str, age:int) -> None:
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age

class Student(Person):
    
    def __init__(self, id: str,  cf: str, name: str, surname: str, age: int) -> None:
        super().__init__(cf, name, surname, age)
        self.id = id
        self.group = None
    
    def withdraw (self):
        if self.group is not None:
            self.group.students.remove(self)
            self.group.limit_students += 1
            self.group = None
            return True
        return False
 
