"""
Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione.
L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. 
La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.
"""
def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    # cancella pass e scrivi il tuo codice
    if conditionA == True:
        return "Operazione permessa"
    else:
        if conditionB == True:
            if conditionC == True:
                return "Operazione permessa"
            else:
                return "Operazione negata"
        else:
            return"Operazione negata"
        

"""
Scrivi una funzione che rimuove tutti i duplicati da una lista, 
contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
"""
def remove_duplicates(list:list) -> list:
    # definidici i parametri, cancella pass e scrivi il tuo codice
    listA : list = []
    
    for i in list:
        if i not in listA:
            listA.append(i)
    
    return listA


"""
Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.
"""
def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    # cancella pass e scrivi il tuo codice
    quale:int = 0
    quanti:int = 0
    
    for k,v in da_rimuovere.items():
        quale += k
        quanti += v
    
    for i in lista:
        if i == quale:
            while quanti > 0:
                quanti-=1
                lista.remove(i)
    return lista


"""
PARTE 1
Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, 
e-mail (facoltativo) e numero di telefono (facoltativo). La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
 
PARTE 2
Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare,
 e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.
"""
def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    # cancella pass e scrivi il tuo codice
    contact :dict = {"profile":name, "email":email,"telefono":telefono}
    return contact

def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    # cancella pass e scrivi il tuo codice
    dictionary["profile"] = name
    if email != None:
        dictionary["email"] = email
    dictionary["telefono"] = telefono
    
    return dictionary


"""
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca 
un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
"""
def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    # cancella pass e scrivi il tuo codice
    empty_dict: dict = {}
    
    for k,v in prodotti.items():
        if v >= 20:
            empty_dict[k] = v - v *10/100

    return empty_dict


"""
Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti 
e aggrega i voti per studente in un nuovo dizionario.
"""
def aggrega_voti(voti: list) -> dict[str:list[int]]:
    # cancella pass e scrivi il tuo codice
    empty_dict:dict = {}
    for i in voti:
        nome = i["nome"]
        voti = i["voto"]
        if nome in empty_dict:
            empty_dict[nome].append(voti)
        else:
            empty_dict[nome] = [voti]
            
            
    return empty_dict

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))