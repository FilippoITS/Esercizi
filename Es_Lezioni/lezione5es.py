# 1. Create a Playlist:
# Write a function called create_playlist() that accepts a playlist name and a variable number of song titles. 
# The function should return a dictionary with the playlist name and a set of songs. Call the function with different numbers of songs to demonstrate flexibility.
# Example: create_playlist("Road Trip", {"Song 1", "Song 2"})
# Write a function called add_like() that accepts a dictionary, the name of a playlist, and a boolean value indicating whether it is liked (True or False).
# This function should return an updated dictionary.
# Example: add_like(dictionary, “Road Trip”, liked=True)

def create_playlist(playlist_name: str , *song_number: set) -> dict :
    
    diz : dict = {}

    diz[playlist_name] = song_number

    return diz

print(create_playlist("Nome Playlist",{"canzone 1" ,"Canzone 2" ,"Canzone3"}))


def add_like(diz: dict , playlista_name: str , bool) -> dict:
    
    diz2 : dict = {}

    for k,v in diz.items():
        diz2[k] = v
    
    diz2["Nome Playlist"] = playlista_name

    diz2["Piaciuto"] = bool

    return diz2

dizionario_prova : dict = create_playlist("Nome Playlist",{"canzone 1" ,"Canzone 2" ,"Canzone3"})

print(add_like(dizionario_prova ,"LALALALALLA" ,False))


#2. Book Collection:
#Write a function called add_book() that accepts an author's name and a variable number of book titles authored by them. 
#This function should return a dictionary where the author's name is the key and the value is a list of their books. 
#Demonstrate this function by adding books for different authors.
#Example: add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])
#Write a function called delete_book() that accepts a dictionary and the name of the author from whom to remove all details. This function should return an updated dictionary.
#Example: delete_book(dictionary, “Mark Twain”)

def add_book (author_name: str , *book_wrote: str ) -> dict:
    diz : dict = {}

    diz[author_name] = book_wrote

    return diz

a =(add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"]))
print(add_book("Artista 1", ["Libro 1", "Libro 2" ,"Libro 3"]))
print(add_book("Artista 2", ["Libro Carino", "Libro Bello" ,"Libro Brutto"]))


def delete_book (dizionario_artista: dict , author_name: str ):
    
    if author_name in dizionario_artista:
        del dizionario_artista[author_name]
         
    return dizionario_artista

print(delete_book(a,"Mark Twain"))


#3. Personal Info:
#Write a build_profile() function that accepts the name , surname,  occupation, location, and age  of a person. Make occupation, location, and age optional parameters.
#Use this function to create profiles for different people, demonstrating how it handles these optional parameters.
#Example: build_profile("John", "Doe", occupation="Developer", location="USA", age=30)

def build_profile (name: str , surname: str , *other_info ) -> None:
    
    print(f"Il nome è {name}\nIl cognome è {surname}\nLa sua occupazione è {other_info[0]}\nLa sua locazione geografica è {other_info[1]}\nMentre la sua età è {other_info[2]}")
        
build_profile("Paolo","Paoli","Disoccupato","Miami","420")


#4. Event Organizer:
#Write a function called plan_event() that accepts an event name, a list of participants, and an hour.
#The function should return a dictionary that includes the event name and a list of the participants. Call this function with varying numbers of participants to plan different events.
#Example: plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],”4pm”)
#Write a function called modify_event() that accepts a dictionary, an event name, and new details to modify an already planned event.
#Example: modify_event(dictionary, "Code Workshop", ["Alice", "Bob", "Charlie"], ”4pm”)

def plan_event (event_name : str , partecipants : list , hour : str) -> dict:

    dizionario_evento : dict = {}

    dizionario_evento["Nome"] = event_name

    dizionario_evento["Partecipanti"] = partecipants

    dizionario_evento["Orario"] = hour

    return dizionario_evento

z = (plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],"19 di Mattina"))


def modify_events (diziozizzio : dict , event_name : str , new_details : str ) -> dict:
    
    #Questa funzione modifica solo il nome dell'evento o l'orario
    
    if event_name in diziozizzio:
        diziozizzio[event_name] = event_name
        return ("Non è cambiato il nome")
    
    elif event_name not in diziozizzio:
        del diziozizzio["Nome"]
        diziozizzio["Nuovo nome evento"] = event_name

    if new_details in diziozizzio:
        return ("Non è cambiata l'ora")
    
    elif new_details not in diziozizzio:
        del diziozizzio["Orario"]
        diziozizzio["Nuovo orario"] = new_details

    return diziozizzio

print(modify_events(z,"NuovoNome","NuovoOrario"))


#5. Shopping List:
#Write a function called create_shopping_list() that accepts a store name and any number of items as arguments.
#It should return a dictionary with the store name and a set of items to buy there. Test the function with different stores and item lists.
#Example: create_shopping_list("Grocery Store", {"Milk", "Eggs", "Bread"})
#Write a function called print_shopping_list() that accepts a dictionary and a store name, then prints each item from that store's shopping list.
#Example: print_shopping_list(dictionary, "Grocery Store")

def create_shop_list ():
    pass