d = {"pippo":2,"pluto":23,"paperino":4}

for i in d:
    print(f'Chiave={i}') #così mi stampo tutte le chievi del dizionario d

keys = list(d.keys()) #creo una lista contenente le ciavi di d

values = list(d.values()) #creo una lista contenente i valori di d

print("Le chiavi:",keys)
print("I valori:",values)

#faccio la somma dei valori del dizionario
i=0
somma=0
while i< len(keys):
    key=keys[i]
    val = d[key]
    #sommare i valori
    somma += val
    i += 1
print(somma)


#faccio la stessa cosa di questo ciclo while fatta con il for
somma_=0
for i in d:
    somma_ = somma_ + d[i]
print(somma_)


#con il ciclo for posso prendere chiave e valore di un dizionario
for CHIAVE,VALORE in d.items():  #però va specificato items 
    print (CHIAVE ,VALORE) #qui ho deciso solo di stamparli ma potevo farci qualsiasi cosa


#creare un nuovo dizionario con le stess chiavi dle primo ma il valore è il rapporto 
# d1={"pippo":0.06,"pluto":0.79,"paperino":0.13}
d1 = {}
for k in d:
    d1[k] = d[k]/somma

print(d1)


#Creare un dizionario il quale abbia il primo key con il valore di una lista con tutti
#i numeri al suo interno pari sommati mentre l'altro i dispari
l=[1,2,3,4,5,2,2,6,3,7,16]

summio:int=[]
for i in l:
    if i %2 == 0 :
         summio.append(i)
summio2 = sum(summio)

basso=[]
for i in l:
    if i %2==1:
        basso.append(i)
basso2=sum(basso)

d2={"somma pari":summio2,"somma dispari":basso2}
print(d2)







