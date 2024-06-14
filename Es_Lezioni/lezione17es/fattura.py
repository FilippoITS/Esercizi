from paziente import Paziente
from dottore import Dottore

class Fattura:

    def __init__(self, pazienti:list[Paziente], dottore:Dottore):
        if dottore.isAValidDoctor() is True:
            self.dottore = dottore
            self.pazienti:int = pazienti
            self.salary:int = 0
            self.fattura:int = len(pazienti)
        else:
             print(f"non è possibile creare una fattura siccome il dottore non è valido")


    def getSalary(self) -> float:
        parcella = self.dottore.getParcel()
        n_pazienti = len(self.pazienti)
        return parcella * n_pazienti


    def getFatture(self) :
        self.fattura = len(self.pazienti)
        return self.fattura


    def addPatient(self, newPatient:Paziente) -> None:
        self.pazienti.append(newPatient)
        self.getSalary()
        self.getFatture()
        print(f"Alla lista del Dottor {self.dottore.get_surname()} è stato aggiunto il paziente {newPatient.getidCode()}") 


    def removePatient(self, idcode:str) -> None:
        for i in self.pazienti:
            if i.getidCode() == idcode:
                self.pazienti.remove(i)
        
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del Dottor {self.dottore.get_surname()} è stato rimosso il paziente {idcode}") 



p1= Paziente("P1","P12","1234")
p2= Paziente("P2","P22","12")
p3= Paziente("P3","P32","1")
p4= Paziente("P4","P42","123")
lista_p= [p1,p2,p3]
d = Dottore("Bello","brutto","Dottorevero",123.4)
d.setAge(35)
a = Fattura(lista_p,d)

print(a.getSalary())
print(a.getFatture())
a.addPatient(p4)
a.removePatient("1234")
