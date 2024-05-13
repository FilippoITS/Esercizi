from person import Student
class Group:

    def __init__(self, name : str, limit_students : int):
        self.name = name
        self.limit_students = limit_students
        self.studens: list[Student] = []
    
    def add_student(self, student= Student):
        if student not in self.studens and self.get_limit_student() > 0:
            self.studens.append(student)
            self.limit_students -= 1
            self.group = self
            return True
        else:
            return False
    
    def get_name(self) -> str:
        return self.name

    def get_limit_student(self) -> int:
        return self.limit_students
