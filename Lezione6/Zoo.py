#3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di
#nutrire tutti gli animali dello zoo. Ogni volta che un animale viene nutrito, 
#la sua salute incrementa di 1% rispetto alla sua salute corrente, 
#ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. 
#Perciò, l'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.
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

class Zoo:

    def __init__(self) -> None:
        pass

        




