# proponuje zadanie programistyczne z obliczeniem pola trojkata

import customtkinter as ctk

class KalkulatorPolaTrojkata(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("KalkulatorPolaTrojkata")
        self.geometry("400x210")
        self.resizable(False,False)
        
        self.podstawa_entry = ctk.CTkEntry(self, placeholder_text="Podstawa", width=100)
        self.wysokosc_entry = ctk.CTkEntry(self, placeholder_text="Wysokość", width=100)
        self.oblicz_pole = ctk.CTkButton(self, text="Oblicz pole", command=self.pole)
        self.pole_wynik = ctk.CTkLabel(self, text="", font=("Roboto", 33))

        self.podstawa_entry.grid(row=0, column=0, pady=20, padx=10)
        self.wysokosc_entry.grid(row=0, column=2, pady=20, padx=10)
        self.pole_wynik.grid(row=1, column=1, pady=20, padx=10)
        self.oblicz_pole.grid(row=2, column=1, pady=20, padx=10)

    def pole(self):
        try:
            podstawa = float(self.podstawa_entry.get())
            wysokosc = float(self.wysokosc_entry.get())
            wynik = (podstawa * wysokosc) / 2
            self.pole_wynik.configure(text=f"Pole: {wynik:.2f}")
        except ValueError:
            self.pole_wynik.configure(text="Proszę wprowadzić liczby!")
        
if __name__ == '__main__':
    app = KalkulatorPolaTrojkata()
    app.mainloop()


# WOW :O
# Fajne i z klasą (Hehe, bo klasa XD)! Bardzo ładnie :D

# (5p / 3p)


# Zadanie 2
def logowanie(popr_login, popr_haslo, n):
    if not isinstance(n, int) or not n > 0:
        return "Error: Argument n musi być liczbą całkowitą dodatnią"
    i = 0
    while i < n: 
        login = input("Podaj login: ")
        haslo = input("Podaj hasło: ")
        if login == popr_login and haslo == popr_haslo:
            return True
        else:
            i += 1
            print("Niepoprawny login lub hasło")
            print(f"Pozostałych prób: {n - i}")
    return False

print(logowanie("123", "abc", 3))

# Sposób jak najbardziej prawiwłowy, dałeś też fajny popis tą funkcją isinstance().
# Elegancko!

# (3/3)



# Zadanie 3

def cyfry(n):
    wynik = 0
    for cyfra in str(abs(n)):
        wynik += int(cyfra)
    return wynik

print(cyfry(12))

# (2/2) Elegancko B)