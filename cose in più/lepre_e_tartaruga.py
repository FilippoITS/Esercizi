import random

print("################################\nBANG !!!!! AND THEY'RE OFF !!!!!\n################################\n")

course: list[str] = []

for i in range(0,70):
    course.append("_") #creo il percorso di 70 caselle

hare:str = "H"
turtle:str = "T"


def turtle_position(stamin:int) -> list[int]: #list[0] -> passo da eseguire, list[1] -> modificatore stamina
    
    stamina : int = stamin
    
    n_random = random.randint(1,10)
    
    passo_veloce = [1,2,3,4,5]
    scivolata = [6,7]
    passo_lento = [8,9,10]
    
    if stamina != 0:
        for n in passo_veloce:
            if n == n_random:               
                if stamina <= 5:
                   print("T -> Recupero di Stamina")
                   return [0, +10]
                else:
                    print("T -> Passo Veloce") 
                    return [3, -5]
        
        for n in scivolata:
            if n == n_random:
                if stamina <= 10:
                    print("T -> Recupero di Stamina")
                    return[0, +10]
                else:
                    print("T -> Scivolata")
                    return [-6, -10]
        
        for n in passo_lento:
            if n == n_random:
                if stamina <= 3:
                    print("T -> Recupero di Stamina")
                    return[0, +10]
                else:
                    print("T -> Passo lento")
                    return [1, -3]
    else:
        return [0, +10]


def hare_position(stamin: int) -> list[int] :
    
    stamina : int = stamin

    n_random = random.randint(1,10)
    
    riposo = [1,2]
    grande_balzo = [3,4]
    grande_scivolata = [5]
    piccolo_balzo = [6,7,8]
    piccola_scivolata = [9,10]

    for n in riposo:
        if n == n_random:
            if stamina <= 90:
                print("H -> Riposo con stamina")
                return [0, +10]
            else:
                print("H -> Riposo senza stamina")
                return [0, +0]
    
    for n in grande_balzo:
        if n == n_random:
            if stamina >= 15:
                print("H -> Grande balzo")
                return [9,-15]
            else:
                print("H -> Riposo")
                return [0, +0]
    
    for n in grande_scivolata:
        if n == n_random:
            if stamina >= 20:
                print("H -> Grande scivolata")
                return [-12,-20]
            else:
                print("H -> Riposo")
                return [0, +0]
    
    for n in piccolo_balzo:
        if n == n_random:
            if stamina >= 5:
                print("H -> Piccolo balzo")
                return [1, -5]
            else:
                print("H -> Riposo")
                return [0, +0]
    
    for n in piccola_scivolata:
        if n == n_random:
            if stamina >= 8:
                print("H -> Piccola scivolata")
                return [-2, -8]
            else:
                print("H -> Riposo")
                return [0, +0]


def course_position(turtle:str, hare:str, course:list[str]):
    contatore: int = 0
    staminaT:int = 100
    staminaH:int = 100
    
    malus: dict[int, int] = {15 : -4, 31 : -15, 58 : -9}
    bonus: dict[int, int] = {20 : +3, 38 : +7, 53 : +13}

    for indexB, bonuS in bonus.items():
        course[indexB] = bonuS
    
    for indexM, maluS in malus.items():
        course[indexM] = maluS

    while True:
        contatore += 1

        if turtle not in course:
            course[0] = turtle
            index_turtle = 0
        else:                             #INDICE TURTLE
            for i in range(len(course)):
                if course[i] == turtle:
                    index_turtle = i
        
        
        if hare not in course:
            course[0] = hare
            index_hare = 0
        else:                             #INDICE HARE
            for i in range(len(course)):
                if course[i] == hare:
                    index_hare = i
        
        
        if contatore % 10 == 0:
            valori_variati : list[int] = variety_ambiental(staminaT,staminaH)
            
            passo_turle = valori_variati[0]
            passo_hare = valori_variati[1]
            
            staminaT = staminaT - valori_variati[3]
            staminaH = staminaH - valori_variati[4]
            print(f"{valori_variati[2]}")
        
        else:
            chiamata_funz_T = turtle_position(staminaT)
            passo_turle = chiamata_funz_T[0]
            stamina_decreaseT = chiamata_funz_T[1]
            staminaT = staminaT + stamina_decreaseT
            
            chiamata_funz_H = hare_position(staminaH)
            passo_hare = chiamata_funz_H[0]
            stamina_decreaseH = chiamata_funz_H[1]
            staminaH = staminaH + stamina_decreaseH

        

        if course[-1] == "_":           
            
                if passo_turle + index_turtle >= 70:
                    course[index_turtle] = "_"
                    course[-1] = turtle
                
                else:
                    if passo_turle < 0 and index_turtle < 5:
                        course[index_turtle] = "_"
                        course[0] = turtle
                        pos_vera = 0
                    else:
                        course[index_turtle] = "_"
                        pos_vera = index_turtle + passo_turle
                        
                        for indexO, bonuS in bonus.items():
                            if pos_vera == indexO:
                                pos_vera += bonuS
                                print(f"Bonus preso da T {bonuS}")
                        
                        for indexM, maluS in malus.items():
                            if pos_vera == indexM:
                                pos_vera += maluS
                                print(f"Malus preso da T {maluS}")
                        
                        course[pos_vera] = turtle
                
                
                if passo_hare + index_hare >= 70:
                    course[index_hare] = "_"
                    course[-1] = hare
                
                else:
                    if passo_hare == -2 and index_hare < 2:
                        course[index_hare] = "_"
                        course[0] = hare
                        pos_veraa = 0        
                    
                    elif passo_hare == -12 and index_hare < 11:
                        course[index_hare] = "_"
                        course[0] = hare
                        pos_veraa = 0
                    
                    else:
                        course[index_hare] = "_"
                        pos_veraa = index_hare + passo_hare
                        
                        for indexO, bonuS in bonus.items():
                            if pos_veraa == indexO:
                                pos_veraa += bonuS
                                print(f"Bonus preso da H{bonuS}")
                        
                        for indexM, maluS in malus.items():
                            if pos_veraa == indexM:
                                pos_veraa += maluS
                                print(f"Malus preso da H {maluS}")
                        
                        course[pos_veraa] = hare
        else:
            print(f"Ha vinto,{course[-1]}")
            break
        
        
        if pos_vera == pos_veraa:
            print("OUCH")
            course[pos_vera] = turtle
            course[pos_veraa] = hare
    
        print(course,"\n")   


def variety_ambiental(staminaT:int, staminaH:int) -> list[int]:
    
    n_random: int = random.randint(1,2)

    if n_random == 1:
        
        passi_veriT: int = turtle_position(staminaT)
        passi_veriH : int = hare_position(staminaH)
        
        passi_penalizzatiT = passi_veriT[0]
        passi_penalizzatiTH = passi_veriH[0]
        
        passi_variatiT : int = passi_penalizzatiT - 1
        passi_variatiH : int = passi_penalizzatiTH - 2
        
        return [passi_variatiT, passi_variatiH, "Giornata di Pioggia", passi_veriT[1], passi_veriH[1]]
    
    else:
        passi_inviariatiT : list[int] = turtle_position(staminaT)
        passi_invariatiH : list[int] = hare_position(staminaH)
        
        return [passi_inviariatiT[0], passi_invariatiH[0], "Giornata Soleggiata", passi_inviariatiT[1], passi_invariatiH[1]]


course_position(turtle,hare,course)
