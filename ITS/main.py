from room import Room
from building import Building
from course import Course
from group import Group
from person import Person
from person import Student


r = Room(name= "213", floor = 2, num_seats = 30)
r1 = Room(name= "312", floor = 3, num_seats= 30)
r2 = Room(name = "612", floor=7, num_seats=5)
r3 = Room(name = "231418", floor=-10, num_seats=20)
print(r,"\n")

b = Building(name = "SMI", address = "Via sierra nevada 60", floors = [-2,6])
print(b,"\n")
b.add_rooms(r)
print(b,"\n")
b.add_rooms(r1)
print(b,"\n")
add = b.add_rooms(r2)
print(add) #la room r2 non è stata aggiunta perchè ha troppi pianiù
add = b.add_rooms(r3)
print(add)

course = Course(name = "python", building=b)
print(course)
# Mi sono fermato al metodo register di Course
