import random
#Es 1
#Create a function that takes a student's name and their scores in different subjects as input.
#The function calculates the average score and prints the student's name, average, and a message indicating whether the student passed the exam (average >= 60) or failed.
#Create a for loop to iterate over a list of students and scores, calling the function for each student.

def student_grade (name:str ,grades:list):
    
    counter:float = 0
    
    a = sum(grades)
    
    for i in range(len(grades)):
        counter +=1
    
    media_totale:float = a / counter

    print(f"La media di {name} è {media_totale}")
    
    if media_totale >= 60:
        print(f"{name} ha passato l'esame")
    else:
        print(f"{name} non ha passato l'esame")

voti_di_giovanni:list = [63 ,80 ,46 ,65 ,54]
voti_di_paolo:list = [100 ,99, 98, 87]
student_grade("Giovanni" ,voti_di_giovanni)
student_grade("paolo" ,voti_di_paolo)

   

#Es 3
#Create a function that defines a product with a name, price, and quantity.
#Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
#The function should calculate the cart total and apply any discounts or taxes.
#Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.

def product_info (name:str ,price:float ,quantity:float):
    
    product:dict= {"maglietta":10 ,"pantalone":18 ,"giacca":35}
    
    a = input(f"Decidi cosa vuoi comprare, scrivere solo il nome dell'oggetto che si vuole acquistare \n{product}\n")
    
    carrello:float = 0
    
    if a == "maglietta":
        carrello += 10
    elif a== "pantalone":
        carrello += 15
    elif a == "giacca":
        carrello += 35
    

    print("Se vuoi hai la possibilità di ottenere uno sconto del 50% se acquisti tutti i capi \n")

    b = input("Scrivere si se vuoi procedere con questa offerta ,altrimenti scrivere no \n")
    
    roba_scontata:float = 0
    
    
    if b == "si":
        roba_scontata += 30
        print(f"Il prezzo compreso di sconto viene: {roba_scontata} euro")
    elif b == "no":
        print(f"Il prezzo totale allora è {carrello} euro")
product_info("ciao",23,33)



#Es 6
#Create a function that generates a random password with a specified length and desired character types
#(lowercase letters, uppercase letters, numbers, symbols).
#Allow the user to specify the password length and desired character types.
#Generate and return a random password that meets the user's criteria.

def random_password (script:str) -> str:
    
    print("In questo programma deciderai la tua password randomica")
    
    i = input("Rispondere a questo input con una parola di quante lettere si vuole la Password \n quindi se volete una password da otto caratteri: scriverete AAAAAAAA\n")
    
    emptyList:list = []
    emptyList2:list = []
    
    for x in range(len(i)):
        emptyList.append("A")
    
    for i in emptyList:
        ran = random.randint(1,26)
        if  ran == 1:
            emptyList2.append("a")
        elif ran == 2:
            emptyList2.append("b")
        elif ran == 3:
            emptyList2.append("c")
        elif ran == 4:
            emptyList2.append("d")
        elif ran == 5:
            emptyList2.append("e")
        elif ran == 6:
            emptyList2.append("f")
        elif ran == 7:
            emptyList2.append("g")
        elif ran == 8:
            emptyList2.append("h")
        elif ran == 9:
            emptyList2.append("i")
        elif ran == 10:
            emptyList2.append("l")
        elif ran == 11:
            emptyList2.append("m")
        elif ran == 12:
            emptyList2.append("n")
        elif ran == 13:
            emptyList2.append("o")  
        elif  ran == 14:
            emptyList2.append("p")
        elif ran == 15:
            emptyList2.append("q")
        elif ran == 16:
            emptyList2.append("r")
        elif ran == 17:
            emptyList2.append("s")
        elif ran == 18:
            emptyList2.append("t")
        elif ran == 19:
            emptyList2.append("u")
        elif ran == 20:
            emptyList2.append("v")
        elif ran == 21:
            emptyList2.append("z")
    
    print("per caso vorresti dei caratteri speciali come lettere maiuscole mischiate con minuscole? (questa scelta ridarà la possibilità di scegliere quanti caratteri si vogliono)")
    
    pop = input("Scrivere una frase da quanti caratteri speciali si vogliono altrimenti scrivere 'no'\n")
    
    if pop == "no":
        passN = str(emptyList2)
        print(f"Ecco la tua password : {passN}")
    else:
        emptyList2.clear()
        for i in range(len(pop)):
            ran = random.randint(1,42)
            if  ran == 1:
                emptyList2.append("a")
            elif ran == 2:
                emptyList2.append("b")
            elif ran == 3:
                emptyList2.append("c")
            elif ran == 4:
                emptyList2.append("d")
            elif ran == 5:
                emptyList2.append("e")
            elif ran == 6:
                emptyList2.append("f")
            elif ran == 7:
                emptyList2.append("g")
            elif ran == 8:
                emptyList2.append("h")
            elif ran == 9:
                emptyList2.append("i")
            elif ran == 10:
                emptyList2.append("l")
            elif ran == 11:
                emptyList2.append("m")
            elif ran == 12:
                emptyList2.append("n")
            elif ran == 13:
                emptyList2.append("o")  
            elif  ran == 14:
                emptyList2.append("p")
            elif ran == 15:
                emptyList2.append("q")
            elif ran == 16:
                emptyList2.append("r")
            elif ran == 17:
                emptyList2.append("s")
            elif ran == 18:
                emptyList2.append("t")
            elif ran == 19:
                emptyList2.append("u")
            elif ran == 20:
                emptyList2.append("v")
            elif ran == 21:
                emptyList2.append("z")
            elif  ran == 22:
                emptyList2.append("A")
            elif ran == 23:
                emptyList2.append("B")
            elif ran == 24:
                emptyList2.append("C")
            elif ran == 25:
                emptyList2.append("D")
            elif ran == 26:
                emptyList2.append("E")
            elif ran == 27:
                emptyList2.append("F")
            elif ran == 28:
                emptyList2.append("G")
            elif ran == 29:
                emptyList2.append("H")
            elif ran == 30:
                emptyList2.append("I")
            elif ran == 31:
                emptyList2.append("L")
            elif ran == 32:
                emptyList2.append("M")
            elif ran == 33:
                emptyList2.append("N")
            elif ran == 34:
                emptyList2.append("O")  
            elif  ran == 35:
                emptyList2.append("P")
            elif ran == 36:
                emptyList2.append("Q")
            elif ran == 37:
                emptyList2.append("R")
            elif ran == 38:
                emptyList2.append("S")
            elif ran == 39:
                emptyList2.append("T")
            elif ran == 40:
                emptyList2.append("U")
            elif ran == 41:
                emptyList2.append("V")
            elif ran == 42:
                emptyList2.append("Z")           

    print("se vuoi posso darti la password, altrimenti posso aggiungere dei numeri  casuali alla fine")
    
    popipopi = input("Scrivere una frase da quanti caratteri speciali si vogliono altrimenti scrivere 'no'\n")

    if popipopi == "no":
        passNN = str(emptyList2)
        print(f"Ecco la tua password : {passNN}")
    else:
        for i in range(len(popipopi)):
            ran = random.randint(0,9)
            emptyList2.append(ran)
            passNNN = str(emptyList2)
        print (f"Ecco la tua password : {passNNN}")

random_password("a")



#Es 8
#Create a function that simulates an ATM machine.
#Initialize an account with a starting balance.
#Allow the user to perform transactions such as deposit, withdraw, and check balance.
#Validate transactions against the account balance and available funds.
#Provide appropriate feedback to the user for each transaction.

def atm_machine (actual_balance:float):

    
    balance:float = float(actual_balance)

    print("Ciao questa è la tua banca che operazione desideri fare oggi?")
    
    dwc = input("1 - Deposita soldi\n2 - Ritira soldi\n3 - Controlla quanti soldi ci sono nel conto\nScrivere il numero dell'operazione da fare\n ")
    
    if dwc == "1":
        d = input("Selezionare la cifra desiderata\n")
        d_int = float(d)
        balance += d_int
                
    elif dwc == "2":
         w = input("Selezionare la cifra desiderata\n")
         w_int = float(w)
         if w_int > balance:
            print("error")
                
         else:
            balance -= w_int
                
    elif dwc == "3":
        print(f"Il tuo saldo è questo {balance}")
            
    dwc2 = input("Se vuoi fare altre azioni scrivi\n1 - Deposita soldi\n2 - Ritira soldi\n3 - Controlla quanti soldi ci sono nel conto\n altrimenti scrivi 'no'\n ")

    if dwc2 == "1":
        d = input("Selezionare la cifra desiderata\n")
        d_int = float(d)
        balance += d_int
    elif dwc2 == "2":
        w = input("Selezionare la cifra desiderata\n")
        w_int = float(w)
        if w_int > balance:
            print("error")
        else:
            balance -=w_int
    elif dwc2 == "3":
            print(f"Il tuo saldo è questo {balance}")
    elif dwc2 == "no":
            print("Arrivederci")

atm_machine(8000)



#Es 2
#Create a function that generates a random number within a range specified by the user.
#Prompt the user to guess the number within a specified maximum number of attempts.
#Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
#Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.

random_number:int = random.randint(1,9)

def guess_the_number (random_number:int):
    
    print("\nIn questa funzione dovrai provare ad indovinare un numero random generato dal pc :)")
    
    a = input("Ti sto dando la prima di 3 possibilità per indovinare, scrivi un numero dal 1 al 9\n---> ")
    a_int = int(a)
    
    if a_int == random_number:
        print("Che mostro ci sei riuscito al primo tentativo")
    
    if a_int < random_number:
        print("il numero da te scelto è piccolo")
    elif a_int > random_number:
        print("il numero da te scelto è grande")
    
    b = input("Seconda possibilità (usa il suggerimetno da me dato)\n---> ")    
    b_int = int(b)
    
    if b_int == random_number:
        print("Bravo ci sono voluti solamente due tentativi")
    
    if b_int > random_number:
        print("Il tuo numero è più grande")
    elif b_int < random_number:
        print("Il tuo numero è più piccolo")
    
    c = input("Questa è la tua ultima chance, hai anche avuto due suggerimenti!!\n---> ")
    c_int = int(c)

    if c_int == random_number:
        print("Sei stato un po lentino ma ci sei riuscito")

    if c_int > random_number:
        print(f"Mi dispiace ma hai fallito, il numero era ->{random_number} ")
    elif c_int < random_number:
        print(f"Mi dispiace ma hai fallito, il numero era ->{random_number} ")
    
    

    
guess_the_number(random_number)



#Es 7
#Create a function that converts a given integer to its Roman numeral representation.
#Handle numbers from 1 to 3999.
#Use a combination of string manipulation and conditional statements to build the Roman numeral.

def given_to_roman (given_number:int):
    


    given_list:list = []
    
    for i in given_number:
        k = int(i)
        given_list.append(k)
    
    given_list.reverse()
    
    numero_romano:list = []

    if given_list[3] == 3:
        numero_romano.append("MMM")
    elif given_list[3] == 2:
        numero_romano.append("MM")
    elif given_list[3] == 1:
        numero_romano.append("M")
        
    
    
    if  given_list[2] == 9:
                numero_romano.append("CM")
    elif  given_list[2] == 8:
                numero_romano.append("DCCC")
    elif  given_list[2] == 7:
                numero_romano.append("DCC")
    elif  given_list[2] == 6 :
                numero_romano.append("DC")
    elif  given_list[2] == 5 :
                numero_romano.append("D")
    elif  given_list[2] == 4 :
                numero_romano.append("CD")
    elif  given_list[2] == 3 :
                numero_romano.append("CCC")
    elif  given_list[2] == 2 :
                numero_romano.append("CC")
    elif  given_list[2] == 1:
                numero_romano.append("C")
    
    if  given_list[1] == 9:
                numero_romano.append("XC")
    elif  given_list[1] == 8:
                numero_romano.append("LXXX")
    elif  given_list[1] == 7:
                numero_romano.append("LXX")
    elif  given_list[1] == 6 :
                numero_romano.append("LX")
    elif  given_list[1] == 5 :
                numero_romano.append("L")
    elif  given_list[1] == 4 :
                numero_romano.append("XL")
    elif  given_list[1] == 3 :
                numero_romano.append("XXX")
    elif  given_list[1] == 2 :
                numero_romano.append("XX")
    elif  given_list[1] == 1:
                numero_romano.append("X")
    
    if  given_list[0] == 9:
                numero_romano.append("IX")
    elif  given_list[0] == 8:
                numero_romano.append("VIII")
    elif  given_list[0] == 7:
                numero_romano.append("VII")
    elif  given_list[0] == 6 :
                numero_romano.append("VI")
    elif  given_list[0] == 5 :
                numero_romano.append("V")
    elif  given_list[0] == 4 :
                numero_romano.append("IV")
    elif  given_list[0] == 3 :
                numero_romano.append("III")
    elif  given_list[0] == 2 :
                numero_romano.append("II")
    elif  given_list[0] == 1:
                numero_romano.append("I")
     
           
    
    print(f"Il numero romano viene : {numero_romano} ")
    
    given_list.reverse()
    print(f"Mentr il numero da te dato era : {given_list}")

given_to_roman("1972")
