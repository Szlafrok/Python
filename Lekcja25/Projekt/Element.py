import pygame

from projekt import file_path

class Obraz(): # Klasa pomocnicza
    def __init__(self, sciezka):
        self.obraz = pygame.image.load(sciezka)

class Element(): # Klasa główna
    def __init__(self, typ):
        self.wybrany = 0
        self.lista_obrazow = []

        for i in range(1, 4):
            sciezka = f'{file_path}{typ}{i}.png' # Lekcja25/Projekt/images/head1.png
            wczytany_obraz = Obraz(sciezka)
            self.lista_obrazow.append(wczytany_obraz)

    def wybierzNastepny(self):
        self.wybrany += 1
        if self.wybrany >= 3:
            self.wybrany = 0

    def wybranyObraz(self):
        return self.lista_obrazow[self.wybrany].obraz
    

class NakrycieGlowy(Element):
    def __init__(self):
        super().__init__('head')

# Ubranie

# Oczy

# Bron