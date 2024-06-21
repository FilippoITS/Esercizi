from film import Film
from movie_genere import Azione, Drammatico, Commedia


class Noleggio:

    def __init__(self, lista_film:list[Film]) -> None:
        self.films:list[Film] = lista_film
        self.rented_film = {}
    

    def isAvaible(self, film:Film) -> bool:
        
        if film in self.films:
            print(f"Il film scelto : {film.getTitle()} è presente")
            return True 
        else:
            print(f"Il film scelto : {film.getTitle()} non è presente")
            return False


    def rentAMovie(self, film:Film, clientId:int) -> None:
        if film in self.films:
            self.films.remove(film)
            if clientId not in self.rented_film:
                self.rented_film[clientId] = []
            self.rented_film[clientId].append(film)
            print(f"Il cliente ha {clientId} ha prenotato il fiml {film.getTitle()}")
        else:
            print(f"Il film : {film} non è disponibile in catalogo ")
    

    def giveBack(self, film:Film, clientID:int, days:int) -> None:
        if film in self.rented_film[clientID]:
            self.rented_film[clientID].remove(film)
            self.films.append(film)
            print(f"Il cliente: {clientID} deve pagare una penale per il film : {film.getTitle()} di {film.getPenale() * days} euro")
        else:
            print(f"Il cliente non ha noleggiato il film : {film.getTitle()}")

    
    def printMovies(self) -> None:
        s: str = "|"
        for i in self.films:
            s +=f"{i.getTitle()} - {i.getGenere()}| "           
        print(s) 


    def printRentMovies(self, clientID:int) -> None:
        if clientID not in self.rented_film.keys():
            print(f"Il cliente : {clientID}, non ha mai noleggiato film)")
            return
        print(f"Il cliente : {clientID}, sta noleggiando questi film {self.rented_film[clientID]}")
        

a = Drammatico(12,"Ciao")
b= Commedia(122, "CICCICIICICICJIICICIC")

n = Noleggio([a,b])
n.isAvaible(a)
n.rentAMovie(a, 1289)
n.rentAMovie(b, 1289)
print(n.rented_film)
n.printMovies()
n.printRentMovies(1289)