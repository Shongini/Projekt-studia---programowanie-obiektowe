class Zegarek:
    Marka = ""
    Rokprodukcji = ""
    Kolor = ""

    def __init__(self,marka,rokprodukcji,kolor):
        self.marka = marka
        self.rokprodukcji = rokprodukcji
        self.kolor = kolor

    def producent(self):
        print("To Zegarek marki", self.marka)

    def wyprodukowanie(self):
        if self.rokprodukcji >= 2022-2004:
            print("Twój zegarek osiągnał pełnoletność.")
        else:
            print("Twój zegarek powinien mieć prawnego opiekuna.")

    def barwa(self):
        if self.kolor == "Czarny":
            print("Jest dzisiaj w kiepskim humorze.")
        else:
            print("Uwielbia być przez Ciebie noszony.")

Przyjaciel = Zegarek("Omega",25, "Czarny")
print("Obiekt -", Przyjaciel.marka, Przyjaciel.rokprodukcji,"letni", Przyjaciel.kolor, "\n")

Przyjaciel.producent()
Przyjaciel.wyprodukowanie()
Przyjaciel.barwa()
