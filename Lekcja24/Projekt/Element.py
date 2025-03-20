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
            sciezka = f'{file_path}{typ}{i}.png'
            wczytany_obraz = Obraz(sciezka)
            self.lista_obrazow.append(wczytany_obraz)