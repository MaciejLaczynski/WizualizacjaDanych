class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        self.pensja = pensja
    def przedstaw_sie(self):
        return "Nazywam się {} {} i zarabiam {} miesięcznie".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):
    def przedstaw_sie(self):
        return "Nazywam się {} {}, jestem menadżerem i zarabiam {} miesięcznie".format(self.imie, self.nazwisko, self.pensja)


jan = Pracownik("Jan", "Górski", 1700)
eustachy = Menadzer("Eustachy", "Motyka", 12000)

print(jan.przedstaw_sie())
print(pawel.przedstaw_sie())
print('--------------------------------------------------')
print('isinstance(jozek, Osoba):', isinstance(jozek, Osoba))
print('isinstance(jozek, Pracownik):', isinstance(jozek, Pracownik))
print('isinstance(jozek, Menadzer):', isinstance(jozek, Menadzer))
print('--------------------------------------------------')
print('isinstance(adrian, Osoba):', isinstance(adrian, Osoba))
print('isinstance(adrian, Pracownik):', isinstance(adrian, Pracownik))
print('isinstance(adrian, Menadzer):', isinstance(adrian, Menadzer))
print('--------------------------------------------------')
print('issubclass(Pracownik, Osoba):', issubclass(Pracownik, Osoba))
print('issubclass(Menadzer, Osoba):', issubclass(Menadzer, Osoba))
print('issubclass(Osoba, Pracownik):', issubclass(Osoba, Pracownik))
print('issubclass(Osoba, Menadzer):', issubclass(Osoba, Menadzer))
print('issubclass(Menadzer, Pracownik):', issubclass(Menadzer, Pracownik))
print('issubclass(Pracownik, Menadzer):', issubclass(Pracownik, Menadzer))