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
        if 2022 - int(self.rokprodukcji) >= 2022-2004:
            print("Twój Przyjaciel osiągnał pełnoletność.")
        if int(self.rokprodukcji) > 2022:
            print("Twój Przyjaciel chyba jeszcze nie został wyprodukowany :)")
        else:
            print("Twój Przyjaciel powinen mieć prawnego opiekuna.")

    def barwa(self):
        if self.kolor == "Czarny":
            print("Jest dzisiaj w kiepskim humorze.")
        else:
            print("Uwielbia być przez Ciebie noszony.")

Przyjaciel = Zegarek(input("Podaj Marke Zegarka: "), int(input("Podaj Rok Produkcji: ")), input("Podaj Kolor: "))

print ("Obiekt - Zegarek", Przyjaciel.marka,",", Przyjaciel.rokprodukcji,"Rok Produkcji",",","Kolor:", Przyjaciel.kolor, "\n")

Przyjaciel.producent()
Przyjaciel.wyprodukowanie()
Przyjaciel.barwa()