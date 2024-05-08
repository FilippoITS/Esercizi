class Zoo:

    def __init__(self) -> None:
        self.recinti = Recinto
        self.guardiani = Guardiano


class Animal:
    
    def __init__(self, name:str, species:str, age:int,
                       whidt:int, height:int,
                       preferred_habitat:str) -> None:
        self.name = name
        self.species = species
        self.age = age
        self.whidt = whidt
        self.height = height
        self.preferred_habitat = preferred_habitat       
        self.healt = 100 * 1/age
        self.animals = []
    
    def __str__(self) -> str:
        return f"{self.name}: specie={self.species}, età={self.age}-anni, larghezza={self.whidt}, 
        lunghezza={self.height}, Habitat Preferibile={self.preferred_habitat}, Salute={self.healt}"

gallina = Animal("Gallina", "Gallus", 8, 20, 45, "normale")
orso_polare = Animal("Orso Polare", "Orso", 4, 70, 220, "freddo")
leone = Animal("Leone", "???", 23, 45, 115, "caldo")
pappagallo = Animal ("Pappagallo", "Ara", 56, 5, 5, "caldo")


class Fence:
    
    def __init__(self, area:int, temperature:int, habitat:str) -> None:
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
    
    def __str__(self) -> str:
        return f"{self.dimnesioni}(Metri),{self.temperatura}(Gradi),{self.habitat}(Habitat) "


class ZooKeeper:
    
    def __init__(self, name_k:str, surname:str, id:int) -> None:
        self.name_k = name_k
        self.surname = surname
        self.id = id
    
    def add_animal(self, animal_to_add:str, fence:str) -> None:
        self.Animals: list[Animal] = []
        self.Animals.append(animal_to_add)
    
    def remove_animal(self):
        pass

    def feed_animal(self, food_to_feed:int):
        pass



        




