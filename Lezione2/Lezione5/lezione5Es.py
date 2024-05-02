"""Scrivi una funzione che accetti tre parametri: username, password e 
status di attivazione dell'account (attivo/non attivo). 
L'accesso è consentito solo se il nome utente è "admin",
la password corrisponde a "12345" e l'account è attivo. 
La funzione ritorna "Accesso consentito" oppure "Accesso negato"."""

def check_access(username: str, password: ..., is_active: bool) -> str:
    # cancella ... è definisci il tipo di dato per password, successivamente cancella pass e scrivi il tuo codice
    a = "Accesso consentito"
    b = "Accesso negato"
    if username == "admin":
        if password == "12345":
            if is_active == True:
                return a
            else:
                return b
        else:
            return b
    else:   
        
        return b
print(check_access("admin","12345",True))


"""Scrivi una funzione che ritorna il valore massimo, 
minimo e la media di una lista di numeri interi."""

def list_statistics(numbers: list[int]) -> float :
    # cancella ... e definisci il tipo del dato di ritorno, successivamente cancella pass e scrivi il tuo codice
    più_grande:list = []
    più_piccolo:list = []

    più_grande.append(max(numbers))
    più_piccolo.append(min(numbers))
    
    a = sum(numbers)
    counter: int = 0
    for i in range(len(numbers)):
        counter += 1
    media: float = a/counter
     
    più_grande1 : int = int(più_grande[0])
    più_piccolo1 : int = int(più_piccolo[0])
    
        
    return(più_grande1,più_piccolo1,media)


"""Scrivi una funzione che riceve un numero e 
stampa un conto alla rovescia da quel numero a zero."""

def countdown(n: int) -> int:
    # cancella pass e scrivi il tuo codice
    counter : int = n
    while 0 <= counter:
        print(counter)
        counter -=1


"""Scrivi una funzione che, 
dato un insieme e una lista di numeri interi da rimuovere, 
ritorni un nuovo insieme senza i numeri specificati nella lista."""

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    # cancella pass e scrivi il tuo codice
    
    emptyList: list = []
    
    for i in original_set:
        if i in elements_to_remove:
            None
        elif i not in elements_to_remove:
            emptyList.append(i)
    
    emptySet: set = set(emptyList)
    return emptySet


"""Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, 
mantenendo l'ordine originale degli elementi."""

def remove_duplicates(lista:list) -> list:
    # definidici i parametri, cancella pass e scrivi il tuo codice
    
    lista2:list = []
    
    for i in lista:
        if i not in lista2:
            lista2.append(i)
    
    return(lista2)


"""Scrivi una funzione che converte una temperatura da gradi Celsius a 
Fahrenheit e viceversa a seconda del parametro to_fahrenheit. 
Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit.
"""

def convert_temperature(celsius:float ,B = True) -> float:
    # cancella ... e definisci i parametri della funzione, successivamente cancella pass e scrivi il tuo codice
    
    res: float = 0
    
    if B == True:
        res = celsius *9/5 +32
    elif B == False:
        res = celsius - 32 
        res = res*5/9
    return res


"""Scrivi una funzione che unisce due dizionari.
 Se una chiave è presente in entrambi, somma i loro valori."""

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    # cancella pass e scrivi il tuo codice
    
    for k,y in dict1.items():
        if k in dict2:
            dict1[k] += dict2[k]
    
    for k,y in dict1.items():
        if k not in dict2.items():
            dict2[k] = y
    
    b = sorted(dict2.items())
    
    dict3: dict = {}
    
    for k,v in b:
        dict3[k] = v
        
    return dict3 


"""Scrivi una funzione che, data una lista, 
ritorni un dictionary che mappa ogni elemento 
alla sua frequenza nella lista."""

def frequency_dict(elements: list) -> dict:
    # cancella pass e scrivi il tuo codice
    
    emptyList: list =[]
    
    diz : dict = {}
    
    for i in elements:
        if i not in diz:
            diz[i] = 0
    
    for i in elements:
        if i in diz:
            diz[i] += 1
            
            
            
    return(diz)



"""Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude."""

def check_parentheses(expression: str) -> bool:
    # cancella pass e scrivi il tuo codice
    
    emptyList:  list = []
    
    for i in expression:
        if i == "(":
            emptyList.append(i)
        
        elif i == ")":
            if not emptyList:
                return False
            emptyList.pop()
    
    return not emptyList


"""Scrivi una funzione che conta e ritorna quante volte un 
elemento appare isolato in una lista di numeri interi. 
Un elemento è considerato isolato se non è affiancato 
sia a destra che a sinistra da elementi uguali."""

def count_isolated(lista:list) -> int:
    # cancella ... e definisci parametri e tipo di dato, successivamente cancella pass e scrivi il tuo codice
    
    counter:int = 0
    
    if len(lista) == 0:
        return counter
    else:
        
        if lista[0] != lista[1]:
            counter += 1
        
        if lista[-1] != lista[-2]:
            counter += 1
        
        for i in range(1,len(lista)-1):
            if lista[i] != lista[i-1] and lista[i] != lista[i+1]:
                counter += 1
    
        return counter