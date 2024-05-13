#8-1
def  display_message (a:int):
    print("in questo capitolo ho imparato ad usare le funzioni")
display_message ("a")


#8-2. Favorite Book
def favorite_book (bookname:str):
    print("my favorite book is", bookname)
libro:int = favorite_book("favorite book")


#8-3. T-Shirt: 
def make_shirt(size:float, text:str):
    print(f"la taglia è: {size} mentre il testo è: {text}")
size: str = "Medium"
text: str = "Brand"
make_shirt(size, text)


#8-4. Large Shirts
#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
#Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
def make_shirt(size:str, text:str):
    if size == "large":
        print ("I love python")
    else:
        print("Non è large")

make_shirt ("large", text)
make_shirt (size, text)


#8-5. Cities: 
#Write a function called describe_city() that accepts the name of a city and its country. 
#The function should print a simple sentence, such as Reykjavik is in Iceland.
#Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.
def describe_city (city:str, country:str):
    print(f"{city} is in {country}")

città: list = ["Roma","Napoli","Madrid"]
for i in città:
    describe_city (i, "Italy")


#8-6. City Names: 
#Write a function called city_country() that takes in the name of a city and its country. 
#The function should return a string formatted like this: "Santiago, Chile". 
#Call your function with at least three city-country pairs, and print the values that are returned.
def city_country (city:str, country:str):
    print(f"{city} , {country}")

city_country ("Santiago", "Chile")
city_country ("Roma", "Italy")
city_country ("Madrid", "Spain")


#8-7. Album: 
"""Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, 
and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. 
Print each return value to show that the  dictionaries are storing the album information correctly. 
Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
If the calling line includes a value for the number of songs, add that value to the album's dictionary. Make at least one new function call that includes the number of songs on an album."""
def make_album (name:str , artist:str , song:float = None):
    album:dict = {name : artist , "Le canzoni sono" : song}
    print(album)
make_album("Album 1" , "Artista 1")
make_album("Album 2" , "Artista 2")
make_album("Album 3" , "Artista 3" , 20)


#8-8. User Albums: 
#Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information,
#call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.
while True:
    #a = input("inserisci il nome: ") 
    #b = input("Scrivi il cognome: ")
    break
#make_album(a, b)


#8-9. Messages: 
#Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.
shortmsg: list = ["Messaggio 1", "Messaggio 2", "Messaggio 3"]
def show_messagges(lista : list):
    for i in lista:
        print(f"i messaggi della lista sono: {i}")
show_messagges(shortmsg)


#8-10. Sending Messages: 
#Start with a copy of your program from Exercise 8-9.
#Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
#After calling the function, print both of your lists to make sure the messages were moved correctly.
def send_messages(lista : list):
    listaCopiata: list = []
    for i in lista:
        print(f"i messaggi sono :{i}")
        listaCopiata.append(i)
    print(listaCopiata)
send_messages(shortmsg)


#8-11. Archived Messages: 
#Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages.
#After calling the function, print both of your lists to show that the original list has retained its messages.
def send_messages(lista : list):
    
    listaCopiata: list = []
    
    for i in lista:
        listaCopiata.append(i)
    
    print(listaCopiata,lista)
send_messages(shortmsg)


#8-12. Sandwiches: 
#Write a function that accepts a list of items a person wants on a sandwich.
#The function should have one parameter that collects as many items as the function call provides,
#and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.
def sandwich_maker (items1:str ,items2:str ,items3:str) :
    
    allitems:list = [items1, items2, items3]
    print(f"il panino ha questi ingredienti {allitems}")
    
sandwich_maker("pane" ,"Salsiccia" ,"Ravioli")
sandwich_maker("pane" ,"hamburger" ,"maionese")
sandwich_maker("pane" ,"pollo fritto" , "ravanelli")


#8-13. User Profile:  
#Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.
#All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
def build_profile(Nome:str ,Age:int ,Hair:str , Weight:int):
    identikit: dict = {"Name": Nome , "Age" : Age , "Hair" : Hair , "Weight" : Weight}
    emptylist:list = []
    for i in identikit.values():
        emptylist.append(i)
    stringa: str = str(f"{emptylist[0]} ,age {emptylist [1]} , hair {emptylist[2]} , weight {emptylist[3]} ")
    return(stringa)

print(build_profile("Filippo Guerriero" ,20 ,"Biondi?" ,"70?"))


#8-14. Cars: 
#Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name.
#It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two 
#other name-value pairs, such as a color or an optional feature. 
#Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) 
#Print the dictionary that’s returned to make sure all the information was stored correctly. 
def car_info(carName:str ,model:str , colore:str , optional:str):
    cars:dict = {"name":carName ,"Model":model ,"color":colore, "optional":optional}
    print(cars)

car_info("Fiat" ,"Panda" ,"Oro" ,"Tutti")


#8-15. Printing Models: 
#Put the functions for the example printing_models.py in a separate file called printing_functions.py.
#Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
from printing_models import print_str
print_str("Stringa")

#8-16. Imports: 
#Using a program you wrote that has one function in it, store that function in a separate file. 
#Import the function into your main program file, and call the function using each of these approaches:
from printing_models import print_str #import module_name
from printing_models import print_str as scrivi_stringa
import printing_models as gg
scrivi_stringa("Stringa")
