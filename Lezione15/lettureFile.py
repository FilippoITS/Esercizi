with open("Lezione15.py/prova.txt"):

    pass




class ContextManager: #Da questa riga in poi faccio quello che in teoria sarebbe il with, quindi non mi serve quando devo usare il with

    def __enter__(self):
        
        print("Risorsa Acquisita")
        
        return self


    def __exit__(self, errore_1, errore_2, errore3):
        
        if errore_1 is not None:
            #teoricamente si dovrebbe stampare il tipo di errore
            pass
        
        print("Risorsa rilasciata")

        return False

with ContextManager() as Manager:

    print("Sono dentro il with")




