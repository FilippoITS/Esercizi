class Animal:
    
    def __init__(self, name:str, species:str, age:int,
                       widht:int, height:int,
                       preferred_habitat:str) -> None:
        self.name = name
        self.species = species
        self.age = age
        self.widht = widht
        self.height = height
        self.preferred_habitat = preferred_habitat       
        self.health = round(100 * (1 / age), 3)
        
      
    def __str__(self) -> str:
        return f"{self.name}: specie={self.species}, età={self.age}-anni, larghezza={self.widht}, lunghezza={self.height}, Habitat Preferibile={self.preferred_habitat}, Salute={self.health}"


class Fence:
    
    def __init__(self, area:int, temperature:int, habitat:str) -> None:
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []
        
    
    def area_remaining(self) -> float:
        single_area_occupation = 0
        for animal in self.animals:
            single_area_occupation += (animal.widht * animal.height)
        
        return self.area - single_area_occupation

    
    def __str__(self) -> str:
        return f"{self.area}(Metri),{self.temperature}(Gradi),{self.habitat}(Habitat) "


class ZooKeeper:
    
    def __init__(self, name_k:str, surname:str, id:int) -> None:
        self.name_k = name_k
        self.surname = surname
        self.id = id
    

    def add_animal(self ,animal: Animal ,fence: Fence) -> None:                              
        if animal in fence.animals:
            print(f"#####Animale Non Aggiunto#####\nNon puoi aggiungere lo stesso animale: ({animal.name})")
        elif animal not in fence.animals:
            if animal.age < 100:
                if animal.preferred_habitat == fence.habitat:
                    animal_occupation = animal.height * animal.widht  
                    if fence.area_remaining() < animal_occupation:
                        print(f"#####Animale Non Aggiunto#####\nL'animale in questione {animal.name} è troppo pesante, non può essere aggiunto all'habitat\n")
                    elif fence.area_remaining() >= animal_occupation:                                                                                                                       
                        fence.animals.append(animal)
                        print(f"#####Animal Aggiunto#####\nL'animale {animal.name} è stato correttamente aggiunto al suo habitat/recinto")
            elif animal.age >= 100:
                print(f"#####Animale Non Aggiunto#####\nL'animale {animal.name} è troppo anziano, purtroppo non verrà aggiunto all'habitat")

    def remove_animal(self, animal: Animal) -> None:
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"#####Animale Rimosso#####\nL'animale {animal.name} è stato rimosso dal suo habitat\nInoltre anche la sua area è stata ripristinata\n")
        elif animal not in self.animals:
            print("Non puoi rimuovere un animale che non c'è\n")


    def feed_animal(self, animal: Animal) -> None: #Da modificare e renderlo che quando richiamato dia da mangiare ad un solo animale.
        new_animal_occupation: float = 0
        for anima in self.fence.animals:
            if anima == animal: 
                if self.fence.area_remaining() >= new_animal_occupation:                    
                    for animal in fence.animals:
                        if animal.health < 100:
                            print(f"\nParametri di {animal.name} prima di essere nutrito\nvita= {animal.health}, larghezza= {animal.widht}, altezza= {animal.height}\n")
                            animal.health = animal.health + animal.health * 2 / 100
                            animal.widht = animal.widht + animal.widht * 2 / 100
                            animal.height = animal.height + animal.height * 2 / 100 
                            print(f"Gli animali si sono nutriti correttamente, parametri di : {animal.name}\nvita= {animal.health}, larghezza= {animal.widht}, altezza= {animal.height}\n")
                        else:
                            print("GLi animali non possono essere nutriti perchè un elemento ha già la salute al massimo")
                else:
                    print("Gli animali non possono mangiare sennò occuperebbero troppo spazio")   


    def clean_fence(self, fence: Fence) -> float:   #da rivedere il tempo di pulizia                                                        
        all_animal_occupation: float = 0
        
        for animal in fence.animals:
            animal_occupation = animal.widht * animal.height
            all_animal_occupation += animal_occupation
        
        if fence.area_remaining() > 0:     
            cleaning_time: float = all_animal_occupation / fence.area_remaining()
            for animal in fence.animals:
                        fence.animals.remove(animal)
                        print(f"#####Tempo Pulizia Habitat#####\nIl tempo impiegato dal Guardiano per pulire il recinto è di {cleaning_time}s")
        elif fence.area_remaining() == 0:
            print(f"#####Tempo Pulizia Habitat#####\nl'area residua è pari a zero restituisco l'area occupata: {fence.area}")


class Zoo:

    def __init__(self, fence: list[Fence], zookeeper: list[ZooKeeper]) -> None:
        self.fences:list = fence
        self.zookeepers:list = zookeeper

    def describe_zoo(self):
        empty_list:list = []
        empty_list2:list = []
        empty_dict: dict = {}
        for fenc in self.fences:
            a = f"###Fence###\narea = {fenc.area}, temperature = {fenc.temperature}, habitat = {fenc.habitat}\n"
            empty_list.append(a)
        for Fence in self.fences:
            for animal in Fence:
                empty_dict[animal.name] = f"specie={self.species}, età={self.age}-anni, larghezza={self.widht}, lunghezza={self.height}, Habitat Preferibile={self.preferred_habitat}, Salute={self.health}"
        for keeper in self.zookeepers:
            b = f"###Zookeper\n name = {keeper.name_k}, surname = {keeper.surname}, ID = {keeper.id}"
            empty_list2.append(b)
        return a,empty_dict,b
        

fence1 = Fence(1000, 20, "Continent")
fence2 = Fence(1000, 20, "Continent")
animal1 = Animal("Scoiattolo", "Blabla", 25, 2, 5, "Continent")
animal2 = Animal("Lupo", "Lupus", 10, 2, 200, "Continent")
animal3 = Animal("lalal", "!laalla", 20, 1, 2, "Continent")
guardiano1 = ZooKeeper("Mario","Rossi",12345)
zing = Zoo([fence1,fence2], guardiano1)

guardiano1.add_animal(animal3,fence1)
guardiano1.add_animal(animal2, fence1)
guardiano1.add_animal(animal3,fence2)
guardiano1.add_animal(animal2, fence2)

print(zing.describe_zoo())