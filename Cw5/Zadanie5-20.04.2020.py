class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)

class Pawnstar(Osoba):
    def __init__(self, imie, nazwisko):
        Osoba.__init__(self, imie, nazwisko)
    def przedstaw_sie(self):
        return "I'm {} {} and this is my Pawn Shop. I work here with my old man, and my son Big Hoss. Everything in here has a story and a price. One thing I learnt after 21 years is you never know WHAT is gonna come through that door.".format(self.imie, self.nazwisko)

class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        self.pensja = pensja
    def przedstaw_sie(self):
        return "Nazywam się {} {} i zarabiam {}zł miesięcznie".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):
    def przedstaw_sie(self):
        return "Nazywam się {} {}, jestem menadżerem i zarabiam {}zł miesięcznie".format(self.imie, self.nazwisko, self.pensja)


jan = Pracownik("Jan", "Górski", 1700)
eustachy = Menadzer("Eustachy", "Motyka", 25000)
rick = Pawnstar("Rick", "Harison")

print(jan.przedstaw_sie())
print(eustachy.przedstaw_sie())
print(rick.przedstaw_sie())
print('--------------------------------------------------')
print('isinstance(jan, Osoba):', isinstance(jan, Osoba))
print('isinstance(jan, Pracownik):', isinstance(jan, Pracownik))
print('isinstance(jan, Menadzer):', isinstance(jan, Menadzer))
print('isinstance(jan, Pawnstar):', isinstance(jan, Pawnstar))
print('--------------------------------------------------')
print('isinstance(eustachy, Osoba):', isinstance(eustachy, Osoba))
print('isinstance(eustachy, Pracownik):', isinstance(eustachy, Pracownik))
print('isinstance(eustachy, Menadzer):', isinstance(eustachy, Menadzer))
print('isinstance(eustachy, Pawnstar):', isinstance(eustachy, Pawnstar))
print('--------------------------------------------------')
print('isinstance(rick, Osoba):', isinstance(rick, Osoba))
print('isinstance(rick, Pracownik):', isinstance(rick, Pracownik))
print('isinstance(rick, Menadzer):', isinstance(rick, Menadzer))
print('isinstance(rick, Pawnstar):', isinstance(rick, Pawnstar))
print('--------------------------------------------------')
print('issubclass(Pracownik, Osoba):', issubclass(Pracownik, Osoba))
print('issubclass(Menadzer, Osoba):', issubclass(Menadzer, Osoba))
print('issubclass(Pawnstar, Osoba):', issubclass(Pawnstar, Osoba))
print('issubclass(Osoba, Pracownik):', issubclass(Osoba, Pracownik))
print('issubclass(Osoba, Menadzer):', issubclass(Osoba, Menadzer))
print('issubclass(Osoba, Pawnstar):', issubclass(Osoba, Pawnstar))
print('issubclass(Menadzer, Pracownik):', issubclass(Menadzer, Pracownik))
print('issubclass(Pracownik, Menadzer):', issubclass(Pracownik, Menadzer))
print('issubclass(Pracownik, Pawnstar):', issubclass(Pracownik, Pawnstar))
print('issubclass(Menadzer, Pawnstar):', issubclass(Menadzer, Pawnstar))