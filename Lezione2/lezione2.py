# Filippo Guerriero
# 18/04/2024

print("Hello World")

#2-3 Scrivere cosa ho fatto e spiegare i passaggi
nome: str = "Eric"
print(f"Hello {nome} , would you like to learn some Python today?")


#2-4 Scrivere cosa ho fatto e spiegare i passaggi
nome_1: str=  "Paolo"
print(nome_1.capitalize(),nome_1.lower(),nome_1.title())


#2-5 Scrivere cosa ho fatto e spiegare i passaggi
frase:str = "Non dire gatto se non ce l'hai nel sacco"
print  (f"'un vecchio saggio una volta disse':{frase}") 


#2-6 Scrivere cosa ho fatto e spiegare i passaggi
saggio: str="Un vecchio saggio una volta disse"
print(saggio,frase)


#3-1 Scrivere cosa ho fatto e spiegare i passaggi
names=["Paolo","Mario","Giorgio","Luigi","Patrizio"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])


#3-2 Scrivere cosa ho fatto e spiegare i passaggi
print(f"Ciao caro amico mio{names[0]},come stai?")
print(f"A grandioso!! ma tu eri{names[1]},vero?")
print(f"Da quanto tempo{names[2]},Come stai?")
print(f"Come sta tua filgia,{names[3]}?")
print(f"Ciao,{names[-1]}")


#3-3 Scrivere cosa ho fatto e spiegare i passaggi
cars=["Bmw","Ferrari","Honda","Fiat"]
print(f"La {cars[0]} la trovo una grande macchina")
print(f"Mentre la {cars[1]} nel settore è una delle migliori")
print(f"Non ho nulla da dire di {cars[2]}")
print(f"Lei invece è la migliore nel campo: {cars[-1]}")


#3-4 fare lista con 3 persone che inviterei a cena e fare una domanda ad ognuna di esse
invited = ["Mario Rossi" , "Matteo Bianchi" , "Tommaso Neri"]
print(f"Ciao {invited[0]},stasera se vuoi puoi venire a cenare da me")
print(f"Come va {invited[1]}? Ti andrebbe di venire a cena da me?")
print(f"Hey {invited[2]}, ti va di rivederci per cena a casa mia questa sera?")


#3-5 da finire
print(f"Purtroppo il sigonre {invited[-1]} non può venire...")
