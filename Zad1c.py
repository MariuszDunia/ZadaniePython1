class kwiat():
    def __init__(self, kolor, nazwa, ksztalt):
        self.kolor = kolor
        self.nazwa = nazwa
        self.ksztalt = ksztalt

def opis():
        print("{} jest {} i {}.".format
            (
            kwiat.kolor, kwiat.nazwa, kwiat.ksztalt
        )
        )

nazwa = input("Wprowadź nazwę kwiata: ")
ksztalt = input("Wprowadź kształt kwiata: ")
kolor = input("Wprowadź kolor kwiata: ")


kwiat = kwiat(nazwa, ksztalt, kolor)
opis()