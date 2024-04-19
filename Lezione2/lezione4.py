#Creo una funzione la quela deve farmi un dizionario{"str":int}
#e restiturmi un dizionariro{"str[d]":int[d]/sum di d1}
def rewrite_dict(d : dict[str,int]):
    somma: list = sum(d.values())
    print(f"La somma è {somma}")
    d1 = {} 
    for k in d :
        d1[k] = d[k] / somma
    return d1

d = {"camicia":12,"Paoletto":21,"papera":43}
output = rewrite_dict(d)
print(output)

#Crea una funzione che prende due parametri e ne fa la sotrazione
#Metodo1
def substract(x:int,y:int):
    z:int=x-y
    return z
output=substract(5,4)
print(output)

#Metodo2
def substract(x:int,y:int):
    z:int=x-y
    
    print(z)
substract(7,2)

#Creare una lista di numeri e calcolare la mediana e farlo tramite funzione
#fatta da me
def median(l: list[float]):
    l.sort
    l1=[]
    if  len(l) > 2 and len(l)/2 != 0 : 
        mid = len(l) // 2
        l4=[mid]
        return l4
        
    else:
        r = l1.append(l[len/2])
        l3 = r/2
        return l3

l = [1,2,4,1,4,5,43,3,4,5,1]
print(f"La mediana della lista {l} è {median(l)}")

#Fatta dal prof
def median2(l:list[float]):
    l.sort
    mid=len(l)//2
    if len(l)%2 != 0:
        mediana=l[mid]
    else:
        mediana=(l[mid]+l[mid-1])/2
    return mediana

print(f"La mediana della lista{l} è {median2(l)}")

#Fare una funzione dove prendo una sequanza cumulativa di una lista
#Sequenza cumulativa: l=[1,2,3,4,5,6] ---> deve diventare 1-2-3-4-5-6
def diff_cum(l: list[float]):
    diff: float = l[0]
    for i in l[1:]:
        diff = diff - i
    print(diff) 

l=[1,2,3,4,5,6]
diff_cum(l)       

def diff_cum2(l: list[float], index: int):
    diff2 = l[index]
    if -len(l) <= index < len(l):
        for i in range(len(l)):
            if i != index:
                diff2 = diff2 - l[i]
    else:
        return "ciao"
        
    return diff2

diff_cum2(l,-124)