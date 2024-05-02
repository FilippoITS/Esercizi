#Per mettere degli elementi di una lista all'intern di un dizionario:
#Basta fare questo
lista: list = ["a" ,"b" ,"c"]
diz:dict = {}

for i in lista:
    diz[i] = 0
#Adesso ho un dizionario così : diz:{"a": 0 , "b": 0 , "c":0}


Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo).
L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo. La funzione ritorna "Accesso consentito" oppure "Accesso negato".

 