#Filippo Guerriero
#23/04/2024

#5-1
"""Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test."""

car:str = "macchina"
dog:str = "cane"
water:str = "acqua"   
error:str = "errore"
python:str = "Daje"

#Those are the  variabiles

print("Is car=='macchina'? I predict True --->",car=="macchina")
print("is car=='peppe'? I prdict False --->",car=='peppe')
print("is dog=='cane'? I predict True --->",dog=="cane")
print("is dog=='gatto'? I predict False --->",dog=="gatto")
print("is water=='acqua'? I predict True --->",water=="acqua")
print("is water=='coca-cola'? I predict False --->",water=="coca-cola")
print("is error=='errore'? I predict True --->",error=="errore")
print("is error=='corretto'? I predict False --->",error=="corretto")
print("is python=='Daje'? I predict True --->",python=="Daje")
print("is python=='daje'? I predict False --->",python=="daje")

#From line 17-28 there are the prediction 


#5-2 More conditional test
print("is error=='ERRORE'ma usando il lower? I predict True --->",
      error.lower()=="ERRORE") 
# 32-34 Tests using the lower() method

smallnum:int = 8
bignum:int = 200
print("Is smallnum > bignum? I predict false--->",smallnum > bignum)
print("Is bignum != smallnum? i predict True_-->",bignum!=smallnum)
print("Is smallnum<bignum? I predict True--->",smallnum<bignum)

#36-40 Numerical tests involving equality and inequality,
#greater than and less than,
#greater than or equal to, and less than or equal to

#parte and e or da finire

lists:list = ["salve","buonase","gianni",12]
if "gianni" in lists:
    print("Gianni è in list",True)
if "Come va" not in lists:
    print("no non c'e",False)

#47-51 Test whether an item is in a list
#Test whether an item is not in a list

#5-3
"""Imagine an alien was just shot down in a game. 
Create a variable called alien_color
and assign it a value of 'green', 'yellow', or 'red'."""

alien_color:str = "rosso"
if "verde"in alien_color: #Write an if statement to test whether the alien’s color is green.
    print("nice you got 5 point") #If it is, print a message that the player just earned 5 points.

if "rosso"in alien_color: #Write one version of this program that passes the if test
    print("5 point for you") #and another that fails.
else:
    None


#5-4
"""Choose a color for an alien as you did in Exercise 5-3,
and write an if-else chain."""

if "verde" in alien_color:                              
    print("you shoot the alien and gained 5 point")#-If the alien’s color is green, 
                        #print a statement that the player just earned 5 points for 
                                                   #shooting the alien.
else:
    print("nice your alien is not green *10 point* ")#-If the alien’s color isn’t green, 
                                #print a statement that the player just earned 10 points

if "rosso" in alien_color:
    print("you shoot the alien and gained 5 point")
else:
    print("nice yout alien is not green *10 point* ")


#5-5
if "verde" in alien_color:
    print("*5 point*")
# If the alien is green, print a message that the player earned 5 points.
elif "giallo" in alien_color:
    print("*10 point*")
# If the alien is yellow, print a message that the player earned 10 points.
else:
    print("*15 point*")
# If the alien is red, print a message that the player earned 15 points.

if "giallo" in alien_color:
    print("*5 point*")
elif "rosso" in alien_color:
    print("*10 point*")
else:
    print("*15 point*")

if "rosso" in alien_color:
    print("*5 point*")
elif "verde" in alien_color:
    print("*10 point*")
else:
    print("*15 point*")
#Write three versiod for the appropriate color alien.


#5-6
age:float = 20
if age < 2 :
    print("é un bambino")
elif 2< age <=4:
    print("Bambino poco più grande")
elif 4< age <=13:
    print("Quasi un adolescente")
elif 13< age <=20:
    print("è un adolescente")
elif 20< age <=65:
    print("è un adulto")
elif age > 65:
    print("è un anziano")


#5-7
favorite_fruit:list = ["Fragole","Ananas","Cocomero"]
if "Fragole" in favorite_fruit:
    print(f"Che buone le {favorite_fruit[0]}")
elif "Mango" in favorite_fruit:
    print("No")
elif "Cocomero" in favorite_fruit:
    print(f"Mi piace molto il {favorite_fruit[-1]}")
elif "Mela" in favorite_fruit:
    print("Una mela la giorno leva il medico di torno")
elif "Anans" in favorite_fruit:
    (f"Mi piace molto l'{favorite_fruit[1]}")


#5-8
people:list = ["Jack","Mark","admin","Paul","Caroline"]
for i in people:
    if i != "admin":
        print(f"Welcome back {i} ")
    else:
        print(f"Hello {i}, would you like to see a status report?")


#5-9 sarò sincero non ho capito


#5-10
current_users:list = ["Giams__","Aofpooop","Gingerino","Spurti","Rimico"]
new_users:list = ["Sarilo","Gingerino","Mortino","Rimico","Ferillo"]
for i in current_users:
    if i in new_users:
        print("Nome già in uso, mettere un altro nickname")
    else:
        print("Questo nome è disponibile")


#5-11
oneToNine:list = [1,2,3,4,5,6,7,8,9,]
for i in oneToNine:
    if i == 1:
        print("1st")
    elif i == 2:
        print("2nd")
    elif i == 3:
        print("3rd")
    else:
        print(f"{i}th")







