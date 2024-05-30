class Libro:

    def __init__(self, titolo:str, autore:str, disponibile:bool = True) -> None:
        self.titolo: str = titolo
        self.autore:str = autore
        self.disponibile = disponibile
    

class Biblioteca(Libro):
    
    def __init__(self) -> None:
        self.libri : list[Libro] = []
    
    def aggiungi_libro(self, libro: Libro) -> str:
        if libro not in self.libri:
            self.libri.append(libro)
        
    def presta_libro(self, titolo:str) -> str:
        for libro in self.libri:
            if libro.titolo == titolo:
                if libro.disponibile == True:
                    libro.disponibile = False
                    print(f"Libro disponibile {titolo}")
                else:
                    print(f"libro {titolo} non disponibile")
    
    def restuisci_libro(self, titolo:str) -> str:
        for libro in self.libri:
            if libro.titolo==titolo:
                if libro.disponibile == False:
                    libro.disponibile = True
                    print(f"il libro {titolo} è stato restituito")
            
    
    def mostra_libri_disponibili(self) -> str:
        libri_disponibili : list[Libro] = []

        for libro in self.libri:
            if libro.disponibile == True:
                libri_disponibili.append(libro.titolo)
        
        if len(libri_disponibili) != 0:
            print(f"I libri disponibili sono : {libri_disponibili}")
            return libri_disponibili       
        else:
            print("Errore, al momento non ci sono libri disponibili")


libro1: Libro = Libro("titolo1","autore1")
libro2: Libro = Libro("titolo2","autore2")
libro3: Libro = Libro("titolo3","autore3")

biblioteca: Biblioteca = Biblioteca()
biblioteca.aggiungi_libro(libro1)
biblioteca.aggiungi_libro(libro2)
biblioteca.aggiungi_libro(libro3)
biblioteca.presta_libro("titolo1")
biblioteca.presta_libro("titolo1")
biblioteca.restuisci_libro("titolo1")
biblioteca.mostra_libri_disponibili()


print("\n","#" * 90,"\n")


class MovieCatalog:

    def __init__(self) -> None:
        self.movies: dict = {}
    
    def add_movie(self, director_name: str, movies: int) -> str:
        
        self.movies[director_name] = movies
        for k in self.movies.keys():
            if k == director_name:
                self.movies[k] = movies
                print("Filmi aggiunti con successo")

    





    