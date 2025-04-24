from enum import Enum

class Kierunek(Enum):
    GORA = 0
    PRAWO = 1
    DOL = 2
    LEWO = 3 # zapisujemy stałe.

    # Dziedziczenie po Enum umożliwia nam odwołanie się później do konkretnej wartości stałej
    # za pomocą self.kierunek.value