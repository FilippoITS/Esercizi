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
    

    def add_movie(self, director_name: str, movies: list[str]) -> str:
    
        for k,v in self.movies.items():
            if director_name == k:
                
                for movie in movies:
                    v.append(movie)
                
                print(f"L'ature = {director_name}| Ora ha questi nuovi film {movies}")
        
        if director_name not in self.movies.keys():
            self.movies[director_name] = movies
            print(f"L'autore = {director_name}| Ha questi film = {movies}")
    

    def remove_movie(self, director_name: str, film_name: str) -> str:

        if len(self.movies[director_name]) == 0:
            del self.movies[director_name]
            print(f"L'autore {director_name} è stato rimosso dal MovieCatalog perchè non ha più film")

        for k,v in self.movies.items():
            if k == director_name:
                if v in self.movies.values():
                    v.remove(film_name)
                    print(f"Il film = {film_name}| è stato rimosso dai film di = {director_name}")
    

    def list_directors(self) -> str:
        lista_autori: list[str] = []
        
        for k in self.movies.keys():
            lista_autori.append(k)
        
        print(f"Gli autori ora presenti nel MovieCatalog sono: {lista_autori}")


    def get_movies_by_directors(self, director_name: str) -> str:
        lista_film: list[str] = []
        
        for k,v in self.movies.items():
            if k == director_name:
                lista_film.append(v)
        print(f"L'autore = {director_name}| Ha questi film = {lista_film}") 


    def search_movies_by_title(self, title: str) -> str:        
        movies_list : list[str] = []

        for list_film in self.movies.values():
            for film in list_film:
                if film[0:len(title)] == title:
                    movies_list.append(film)
        print(f"I film che contengono la parola {title}| Sono = {movies_list}")
                    
                    
a = MovieCatalog()
a.add_movie("Mario", ["Film1", "Film2", "Film3"])
a.add_movie("Mario", ["Film5","Film9"])
a.remove_movie("Mario", "Film3")
a.add_movie("Paolo", ["Filmone"])
a.list_directors()
a.get_movies_by_directors("Mario")
a.search_movies_by_title("Fil")
    





    