from film import Film
"""- Definire i seguenti metodi:

    init(film_list): tale metodo, inoltre,  deve creare un dizionario vuoto chiamato rented_film.
    isAvaible(film): tale metodo deve ritornare True se il film passato come argomento è presente 
nell'inventario del negozio, false in caso contrario. Se il film è disponibile in negozio stampare: 
"Il film scelto è disponibile: {titolo_film}!". Se il film non è disponibile in negozio stamapre: "Il film scelto è disponibile: {titolo_film}!".
    rentAMovie(film, clientID): tale metodo deve gestire il noleggio di un film ed ha come argomenti il 
film da noleggiare ed il codice id del cliente che lo noleggia. Affinché sia possibile noleggiare un film, un film deve essere disponibile in negozio. 
Pertanto, il metodo deve verificare la disponibilità. Nel caso in cui il film richiesto sia disponibile,
rimuoverlo dalla lista dei film disponibili in negozio, poi riempire il dizionario rented_film in questo modo:
        la chiave sarà l'id del cliente che noleggia (id_client)

        il corrispondente valore sarà una lista contenente i film noleggiati da quel cliente.
"""
class Noleggio:

    def __init__(self, lista_film:list[Film]) -> None:
        self.films:list[Film] = lista_film
        self.rented_film = {}
    

    def isAvaible(self, film:Film) -> bool:
        
        if film in self.films:
            print(f"Il film scelto : {film.titolo} è presente")
            return True 
        else:
            print(f"Il film scelto : {film.titolo} non è presente")
            return False


    def rentAMovie(self, film:Film, clientId:int) -> None:
        pass



a = Film(12,"Ciao")
b= Film(122, "CICCICIICICICJIICICIC")
n = Noleggio([a,b])
n.isAvaible(a)