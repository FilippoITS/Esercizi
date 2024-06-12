reader = open("Lettura File/esempio.txt")
print(reader)

try:
    
    reader.readline()
    print("Sono nella try")
    raise Exception("Eccezione")

except Exception:
    
    print("Sono nella except")

finally:
    
    print(reader)
    reader.close()
    print("Sono nella Finally")


with open("Lettura File/esempio.txt") as reader:

    reader.readline()



class ContextManager:

    def __enter__(self):
        
        print("Risorsa acquisita")
        return self
    
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print("Eccezione data da errore")

        return False        


try:

    with ContextManager() as cm:

        print("Ciao")
        print(cm)

except Exception:

        print()



#con questo leggerò l'interno del testo txt
with open("Lettura File/esempio.txt", "r") as reader:

    line = reader.readline()
    line_counter:int = 0
    
    while line != "":
        
        print(f"{line} -number: {line_counter}")
        line =  reader.readline()
        line_counter += 1













