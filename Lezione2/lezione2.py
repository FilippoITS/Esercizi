# Filippo Guerriero
# 18/04/2024

print("Hello World")

#2-3  Personal Message: Use a variable to represent a person’s name,
nome: str = "Eric" # and print a message to that person. Your message should be simple, such as,
print(f"Hello {nome} , would you like to learn some Python today?") # “Hello Eric, would you like to learn some Python today?”


#2-4 Name Cases: Use a variable to represent a person’s name,
nome_1: str=  "Paolo"
print(nome_1.capitalize(),nome_1.lower(),nome_1.title()) # print that person’s name in lowercase, uppercase, and title case.


#2-5 
frase:str = "Non dire gatto se non ce l'hai nel sacco"
print  (f"'un vecchio saggio una volta disse':{frase}") 


#2-6 
saggio: str="Un vecchio saggio una volta disse"
print(saggio,frase)


#3-1 
names=["Paolo","Mario","Giorgio","Luigi","Patrizio"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])


#3-2 
print(f"Ciao caro amico mio {names[0]},come stai?")
print(f"A grandioso!! ma tu eri {names[1]},vero?")
print(f"Da quanto tempo {names[2]},Come stai?")
print(f"Come sta tua filgia, {names[3]}?")
print(f"Ciao, {names[-1]}")


#3-3 
cars=["Bmw","Ferrari","Honda","Fiat"]
print(f"La {cars[0]} la trovo una grande macchina")
print(f"Mentre la {cars[1]} nel settore è una delle migliori")
print(f"Non ho nulla da dire di {cars[2]}")
print(f"Lei invece è la migliore nel campo: {cars[-1]}")


#3-4 
invited = ["Mario Rossi" , "Matteo Bianchi" , "Tommaso Neri"]
print(f"Ciao {invited[0]},stasera se vuoi puoi venire a cenare da me")
print(f"Come va {invited[1]}? Ti andrebbe di venire a cena da me?")
print(f"Hey {invited[2]}, ti va di rivederci per cena a casa mia questa sera?")


#3-5 
print(f"Purtroppo il sigonre {invited[-1]} non può venire...")
invited[-1] = "Paolo Verdi"
print(f"Ciao {invited[0]},stasera se vuoi puoi venire a cenare da me")
print(f"Come va {invited[1]}? Ti andrebbe di venire a cena da me?")
print(f"Hey {invited[2]}, ti va di rivederci per cena a casa mia questa sera?")


#3-6
print(f"Ciao a tutti {invited}, ho un tavolo più grande e posso ospitare più persone :)")
invited.insert(0,"Giacomo Rovini")
invited.insert(2,"Marco Giorgi")
invited.append("Filippo Freschi")
print(f"Siete tutti invitati a casa mia questo venerdì {invited}")


#3-7
print(f"Purtroppo il tavolo non arriverà in tempo, mi dispiace ma devo disdire l'appuntamento {invited}")
invited.pop(0)
print(f"Mi dispiace ma non posso più invitarti {invited[0]}")
invited.pop(0)
print(f"Mi dispiace ma non posso più invitarti {invited[0]}")
invited.pop(0)
print(f"Mi dispiace ma non posso più invitarti {invited[0]}")
invited.pop(0)
print(f"Mi dispiace ma non posso più invitarti {invited[0]}")
del  invited[:]
print(invited)


#3-8
places:list = ["Madrid","Londra","Tokyo","Parigi","Amsterdam"]
print(places)
sorted(places)
print(f"La lista ordinata {places}")
placesreverse = sorted(places, reverse=True)
print(f"La lista ordinata al contrario è {placesreverse}")
places.reverse()
print(f"Ora la liste è così{places}")
places.reverse()
print(f"Adesso invece è così {places}")
places.sort()
print(f"Ora invece torna ordinata{places}")
places.sort(reverse=True)
print(f"Per finire viene così {places}")


#3-9
print("Dovrebbero esserci zero invitati =",len(invited))


#3-10 
leanguages:list = ["Italiano","Francese","Spagnolo","Arabo","Americano"]
sorted(leanguages)
leanguages.reverse
leanguages.pop()
leanguages.insert(0,"Cinese")
otherlanguages: list = ["Giapponese","Thailandese","Foggiano"]
leanguages.append(otherlanguages)
print(leanguages)


#6-1
people: dict= {"First Name":"Matteo","Second Name": "Rossi","Age":22,"City":"Palermo"}
print(f"Il dizionario è :{people}")


#6-2
peopleAndNumbers: dict = {"Matteo":8,"Paolo":19,"Leonardo":17,"Filippo":7,"Sara":3}
print(f"Persone con il loro numero preferito {peopleAndNumbers}")


#6-3
glossary: dict = {"insert()":"inserisce un elemento all'interno di una lista",
                  "append()":"Inserisce un elemento alla fine di una lista",
                  "sort()":"mette in ordine alfabetico gli elementi dentro una lista",
                  "pop()":"leva un elemento all'interno della lista,prende anche indici"}
for k,i in glossary.items():
    print(k,"\n",i)


#6-7
people1: dict = {"First Name":"Luca","Second Name":"Bianchi","Age":19,"City":"Matera"}
people2: dict = {"First Name":"Anotnio","Second Name":"Verdi","Age":17,"City":"Milano"}
peopleList: list=[]
peopleList.append(people)
peopleList.append(people1)
peopleList.append(people2)
for i in peopleList:
    print(i)


#6-8
cat: dict = {"gatto1":"padrone1","gatto2":"padrone2"}
dog: dict = {"cane1":"2padrone","cane2":"2padrone"}
animals: list =[]
animals.append(cat) 
animals.append(dog)   
for i in animals:
    print(i)


#6-9
favorite_places: dict = {"Mario":"Parigi, Londra, Milano","Filippo":"Madrid,Roma,New York","Tommaso":"Torino,Mosca,Oslo"}
for i in favorite_places.items():
    print(i)    


#6-10
peopleAndNumbers["Matteo"]=8,17
peopleAndNumbers["Filippo"]=7,23
peopleAndNumbers["Leonardo"]=17,12
peopleAndNumbers["Sara"]=3,25
peopleAndNumbers["Paolo"]=19,22
for i in peopleAndNumbers.items():
    print (i)


#6-11
cities:dict = {"Roma":{"Country":"italy","Population":"around 6 mil","Fact":"A lot of traffic"}
               ,"Milano":{"Country":"italy","Population":"around 3 mil","Fact":"A lot of smog"}
               ,"Torino":{"Country":"italy","Population":"around 1,5 mil","Fact":"There is a very good egypt museum"}}
for i in cities.items():
    print(i)


#6-12
dog["Cane3"]="padrone3"
dog["Nuovo animale"]= "Nuovo padrone"
print(f"tramite questo dizionario possiamo vedere un elenco di padroni con i loro cani, ed anche un nuovo animale che ha stravolto il dizionario{dog}")
