from room import Room
class Building:
    
    def __init__(self, name: str, address: str, floors: tuple[int, int]) -> None:
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms: list[Room] = []
    
    def add_rooms(self, room: Room) -> bool:
        lower,upper = self.get_floors()
        if room not in self.get_rooms() and lower <= self.get_floors()  <= upper:
            self.rooms.append(room)
            return True
        else:
            return False
    
    def get_name(self) -> str:
        return self.name
    
    def get_address(self) -> int:
        return self.address
    
    def get_floors(self) -> int:
        return self.floors
    
    def get_rooms(self) -> list[Room]:
        return self.rooms
    
    def __str__(self) -> str:
        s: str = f"building(name = {self.get_name()}, address = {self.get_address()}, floors = {self.get_floors()})"
        s += "\n with rooms:\n"
        for room in self.get_rooms():
            s += room.__str__() + "\n"
        return s[:-1]