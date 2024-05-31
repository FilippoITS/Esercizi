class Film:

    def __init__(self, film_name: str, duration: int) -> None:
        self.film_name : str = film_name
        self.duration : int = duration


class Sala:

    def __init__(self, id: int, film: Film, tot_posti: int ) -> None:
        self.id : int = id
        self.film : Film = film
        self.tot_posti : int = tot_posti
        self.posti_prenotati : int = 0
    
    def prenota_posti(self, num_posti) -> None:
        if num_posti < self.posti_disponibili():
            self.posti_prenotati += num_posti
            print("Posti prenotati")
        else:
            print("Non ci sono posti a disposizione")
    
    def posti_disponibili(self) -> str:
        posti_disponibili: int = self.tot_posti - self.posti_prenotati
        print(f"I posti disponibili sono: {self.tot_posti -self.posti_prenotati}")
        return posti_disponibili


class Cinema:
    
    def __init__(self) -> None:
        self.sale : list[Sala] = []
    

    def aggiungi_sala(self, sala: Sala) -> str:
        if sala not in self.sale:
            self.sale.append(sala)
        else:
            print("La sala è gia presente all'interno del cinema")
    

    def prenota_film(self, name: str , num_posti: int) -> str:
        for sala in self.sale:
            if name != sala.film.film_name:
                continue
            else:
                sala.prenota_posti(num_posti)
                print("Il film è stato prenotato con successo")
                return
        
        print("Non puoi prenotare un film che non c'é")


cinema = Cinema()
film1 = Film("Nome1", 90)
film2 = Film("nome2", 28389)
sala1 = Sala(1234, film1, 150)
sala2 = Sala(12345,film2, 2020 )
sala1.prenota_posti(98)
cinema.aggiungi_sala(sala2)
cinema.aggiungi_sala(sala1)
cinema.prenota_film("nome2", 200)
sala1.posti_disponibili()
sala2.posti_disponibili()

print("\n","#" * 90,"\n")


class Prodotto:

    def __init__(self, nome: str, quantita: int) -> None:
        self.nome = nome
        self.quantita = quantita
    
    def __str(self) -> None:
        return f"nome = {self.nome} quantitè = {self.quantita}"


class Magazzino(Prodotto):

    def __init__(self) -> None:
        self.magazzino : list[Prodotto] = []
    
    def aggiungi_prodotto(self, prodotto : Prodotto) -> Prodotto:
        self.magazzino.append(prodotto)
    
    def cerca_prodotto(self, nome: str) -> None:
        for prodotto in self.magazzino:        
            if prodotto.nome == nome:
                print("Il prodotto è disponibile")
                return prodotto
        print("Il prodotto non è disponibile nell'inventario")

    def verifica_disponibilita(self, nome:str) -> str:
        verifica = self.cerca_prodotto(nome)
        if verifica == None:
            print("Il prodotto non è all'intero del magazzino")
        else:
            print(f"Il prodotto è all'interno del magazzino con la quantità = {verifica.quantita} ")


prodotto1: Prodotto = Prodotto("Nome1", 50)
prodotto2: Prodotto = Prodotto("Nome2", 8)
prodotto3: Prodotto = Prodotto("Nome3", 3)
prodotto4: Prodotto = Prodotto("Nome4", 19)
prodotto5: Prodotto = Prodotto("Nome5", 20)        
magazzino1: Magazzino = Magazzino()
magazzino1.aggiungi_prodotto(prodotto1)
magazzino1.aggiungi_prodotto(prodotto2)
magazzino1.aggiungi_prodotto(prodotto3)
magazzino1.aggiungi_prodotto(prodotto4)
magazzino1.cerca_prodotto("Nome1")
magazzino1.cerca_prodotto("Nome6")
magazzino1.verifica_disponibilita("Nome1")
