class Pagamento:

    def __init__(self) -> None:
        self.__pagamento: float = None
    
    
    def setPagamento(self, importo:float) -> None:
        self.__pagamento = importo
    

    def getPagamento(self) -> float:
        return self.__pagamento


    def dettagliPagamento(self) -> None:
        print(f"L'importo del pagamento è: {round(self.__pagamento,2)}")



class PagamentoContanti(Pagamento):

    def dettagliPagamento(self) -> None:
        print(f"L'importo in contanti è di: {round(self.__pagamento,2)}")
    

    def inPezziDa(self) -> None:
        importi:list[float] = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.5, 0.01]
        ammontare:float = self.getPagamento()

        for cifra,index in enumerate(importi):
             if self.getPagamento() / cifra < 1:
                 continue
             else:
                 n_banconote = ammontare // cifra
                 resto = None
        





class PagamentoCartaDiCredito(Pagamento):

    def __init__(self, nome_titolare:str, scadenza:str, numero_carta:int) -> None:
        super().__init__()
        self.titolare = nome_titolare
        self.scadenza = scadenza
        self.numero_carta = numero_carta
    

    def dettagliPagamento(self) -> None:
        print(f"nome titolare: {self.titolare}, scadenza carta: {self.scadenza}, numero carta: {self.numero_carta}\nL'importo è di: {round(self.getPagamento(),2)}")

print(15.12%12)