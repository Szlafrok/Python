class Samochod():

    przebieg = 0
    marka = ""
    model = ""
    kolor = ""
    max_v = 0
    moc_km = 0

    licznik_1 = 0

    def __init__(self, przebieg, marka, model, kolor, max_v, moc_km):
        print("Utworzenie obiektu Samochod...")
        self.przebieg = przebieg
        self.marka = marka
        self.model = model
        self.kolor = kolor
        self.max_v = max_v
        self.moc_km = moc_km
        Samochod.licznik_1 += 1



    def wypisz_dane(self):
        print("DANE AUTKA BRUM BRUM JAK KUBICA")
        print(f"Przebieg: {self.przebieg}")
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Kolor: {self.kolor}")
        print(f"Maks. prędkość: {self.max_v} km/h")
        print(f"Moc silnika: {self.moc_km} koni mechanicznych")

autko = Samochod(5, "Opel", "Kwiat", "Zielony", 350, 600)
autko_2 = Samochod(50, "Citroen", "Cactus", "Szybki", 30, -1)

print(Samochod.licznik_1) # 2

print(autko.marka)

    # Proszę napisać: 
    #     1. zmienne przechowujące informacje o samochodzie
    #     2. metodę do samochodu, która wypisze nam te informacje

    #     3. Proszę utworzyć obiekt typu samochód, podstawić mu dane i wypisać je utworzoną metodą