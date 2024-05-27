import random

print("BANG !!!!! AND THEY'RE OFF !!!!!")
course: list = []

for i in range(0,70):
    course.append("_") #creo il percorso di 70 caselle
   
hare:str = "H"
turtle:str = "T"

def turtle_position(turtle:str, course:list) -> int:
    if turtle not in course:
        course[0] = turtle
    
    n_random = random.randint(1,10)
    
    passo_veloce = [1,2,3,4,5]
    scivolata = [6,7]
    passo_lento = [8,9,10]

    for n in passo_veloce:
        if n == n_random:
            print("Passo Veloce")
            return 3
    
    for n in scivolata:
        if n == n_random:
            print("Scivolata")
            return -6
    
    for n in passo_lento:
        if n == n_random:
            print("Passo lento")
            return 1

def hare_position(hare:str, course:list) -> int:
    if hare not in course:
        course[0] = hare
    
    n_random = random.randint(1,10)
    
    riposo = [1,2]
    grande_balzo = [3,4]
    grande_scivolata = [5]
    piccolo_balzo = [6,7,8]
    piccola_scivolata = [9,10]

    for n in riposo:
        if n == n_random:
            print("Riposo")
            return 0

    for n in grande_balzo:
        if n == n_random:
            print("Grande balzo")
            return 9
    
    for n in grande_scivolata:
        if n == n_random:
            print("Grande scivolata")
            return -12
    
    for n in piccolo_balzo:
        if n == n_random:
            print("Piccolo balzo")
            return 1
    
    for n in piccola_scivolata:
        if n == n_random:
            print("Piccola scivolata")
            return -2

def course_position(turtle:str, hare:str, course:list):
    
    while course[-1] !=  hare or turtle:
        
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
        
        passo_turle = turtle_position(turtle,course)
        passo_hare = hare_position(hare,course)
        
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
                    course[pos_veraa] = hare
        else:
            print(f"Ha vinto,{course[-1]}")
            break
        
        if pos_vera == pos_veraa:
            print("OUCH")
        
        print(course)   
   

    
course_position(turtle,hare,course)


