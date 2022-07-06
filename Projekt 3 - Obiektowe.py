class Zegarek:

    def __init__(self,marka,model, rokprodukcji,kolor,rozmiar):
        self.marka = marka
        self.model = model
        self.rokprodukcji = rokprodukcji
        self.kolor = kolor
        self.rozmiar = rozmiar

    def producent(self):
        print("To Zegarek marki", self.marka, "oznaczenie modelowe", self.model)

    def wyprodukowanie(self):
        if 2022 - int(self.rokprodukcji) >= 2022-2004:
            print("Twój Przyjaciel osiągnał pełnoletność.")
        if int(self.rokprodukcji) > 2022:
            print("Twój Przyjaciel chyba jeszcze nie został wyprodukowany :)")
        else:
            print("Twój Przyjaciel powinen mieć prawnego opiekuna.")

    def barwa(self):
        if self.kolor == "Czarny":
            print("Jego kolor sprawia, że jest dzisiaj w kiepskim humorze.")
        else:
            print("Jego kolor poprawia humor każdej osobie, która go zobaczy.")
    def wielkosc(self):
        if int(self.rozmiar) > 32:
            print("Ze względu na średnicę twojego kumpla na nadgarstku, zgaduję że jesteś mężczyzną.")
        else:
            print("Sądzę że jesteś kobietą, ponieważ tylko one noszą takie drobniutkie zegarki :)")

Marka1 = input("Podaj Marke Zegarka: ")
Model1 = input("Podaj jego oznaczenie modelowe: ")
Rokprodukcji1 = int(input("Podaj Rok Produkcji: "))
Kolor1 = input("Podaj Kolor: ")
Rozmiar1 = input("Podaj Średnicę Zegarka w cm: ")

Przyjaciel = Zegarek(Marka1,Model1,Rokprodukcji1,Kolor1,Rozmiar1)

print ("\n","Obiekt - ", Przyjaciel.marka,"-","Model: ",Przyjaciel.model,",", "Rok Produkcji",Przyjaciel.rokprodukcji,",","kolor zegarka: ", Przyjaciel.kolor,", rozmiar", Przyjaciel.rozmiar, "centymetrów.","\n")

Przyjaciel.producent()
Przyjaciel.wyprodukowanie()
Przyjaciel.barwa()
Przyjaciel.wielkosc()
