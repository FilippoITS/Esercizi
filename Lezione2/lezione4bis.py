def substract_all(x:list[float],y:float):
    res:list = []
    for i in x:
        z=i-y
        res.append(z)
    return res
    

mylist:list = [1,2,3,4,5]
y = 5
ciao = substract_all(mylist,y)
print(ciao)


#Creare una funzione che faccia sottrarre delle liste a vicenda
def substract_list(x:list[float],y:list[float]):
    listsub:list = []
    for i in range(len(x)):
        listsub.append(x[i]-y[i])
    return(listsub)
    

lista1:list = [1,2,3,4,5]
lista2:list = [1,2,3,4,5] 
salve=substract_list(lista1,lista1)
print(salve)


#si può fare anche così semplificandolo con un altra funzione
def add_diff_to_res(x:list[float],y:list[float],lenght:int):
    res:list[float] = []
    for i in range(lenght):
        diff=x[i]-y[i]
        res.append(diff)
    return res
def substract_lists(x:list[float],y:float):
    lenght= min(len(x),len(y))
    res:list[float]=add_diff_to_res(x,y,lenght)
    return res
buonase=substract_lists(lista1,lista2)
print(buonase)


s: str = "La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica, dove le precedenti teorie classiche risultano inadeguate. Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione e la materia sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella, è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg. Esistono numerosi formalismi matematici equivalenti della teoria, come la meccanica ondulatoria e la meccanica delle matrici; al contrario, ne esistono numerose e discordanti interpretazioni riguardo all'essenza ultima del cosmo e della natura, che hanno dato vita a un dibattito tuttora aperto nell'ambito della filosofia della scienza. La meccanica quantistica rappresenta, assieme alla teoria della relatività, uno spartiacque rispetto alla fisica classica, portando alla nascita della fisica moderna. Attraverso la teoria quantistica dei campi, generalizzazione della formulazione originale che include il principio di relatività ristretta, essa è a fondamento di molte altre branche della fisica, come la fisica atomica, la fisica della materia condensata, la fisica nucleare, la fisica delle particelle, la chimica quantistica."
def counter(s:str):
    lunlis:str = len(s) #tutti i caratteri della stinga
    lunpar=len(s.split()) #quante parole ha la stringa
    strfrasi = s.split(".")
    lal=len(strfrasi) #quante frasi ci sono nella stringa 
    parole=s.split()
    paroledistinte= set(parole)
    lenparoledistinte=len(paroledistinte) #quante parole distinte ha la stringa
    
    listafinale=[]
    listafinale.append(lunlis)
    listafinale.append(lal)
    listafinale.append(lunpar)
    listafinale.append(lenparoledistinte)
    return listafinale
        
madaaa=counter(s)
print(madaaa)

#Creo una funzione che da una stringa mi dia un dizionario con quali parole sono contate
#più volte e quali
def word_counter(s:str):
    s:str = s.replace(".","") .replace(",","") .replace(";","") .replace("!","") .replace("?","")
    words:list[str] = s.split()
    d: dict[str,int] = dict() #qua ci sono tutte le parole scritte e quelle scritte 
                              #più volte sono indicate con il numero di quante volte 
                              #state scritte
    d1: dict[str,int] = dict() #qua ci sono tutte le parole ripetute più di una volta
    for i in words:
        if i not in d:
            d[i] = 0
        else:
            d[i] +=1
    
    for k,i in d.items():
        if i >= 1:
            d1[k] = i
    return(d1)       
        
ueue=word_counter(s)
print(ueue)


#Creare una funzione dove se la parola messa è palindroma mi fa true,altrimenti mi da false
def is_palindrome(s:str):
    s:str = s.lower() .replace(" ","")
    i:int = 0
    while i < len(s):
        j = len(s)-(i+1)
        if s[i] != s[j]:
            return False
        i += 1
    return True 
    
arigato=is_palindrome("AmoRoma")
print(arigato)

#Si può fare anche così
def is_palindrome2(s: str):
    s1:str=""
    for i in range(len(s)-1,0,-1):
        s1+=s[i]
    for i in range(len(s1)):
        if s[i] != s1[i]:
            return False
    return True
paperella=is_palindrome2("amoroma")
print(paperella)
