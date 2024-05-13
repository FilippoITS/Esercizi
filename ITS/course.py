from building import Building
class Course:

    def __init__(self, name : str, building : Building ) -> None:
        self.name = name
        self.building: Building = building
        self.groups = []
    
    def get_name(self) -> str:
        return self.name
    
    def get_building(self) -> str:
        return self.building
    
    def __str__(self) -> str:
        return f"course(name = {self.name})" +Building.__str__