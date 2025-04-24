from constants import *
import pygame

class Platforma(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.obraz = pygame.image.load(f"{file_path}pad.png")
        self.porusza_sie = 0
        self.resetuj_pozycje()

    def resetuj_pozycje(self):
        self.rect = pygame.Rect(SZEROKOSC_EKRANU // 2 - 70, WYSOKOSC_EKRANU - 100, 140, 30) # kolejne argumenty: pozycja x, pozycja y, szerokość, wysokość

    def ruszaj_platforma(self, wartosc):
        self.rect.move_ip(PREDKOSC * wartosc, 0) # wartosc: -1 gdy ruch w lewo, 1 gdy ruch w prawo, 0 gdy brak ruchu

        self.porusza_sie = wartosc

        if self.rect.left < 0: self.rect.x = 0
        if self.rect.right > SZEROKOSC_EKRANU: self.rect.x = SZEROKOSC_EKRANU - 140
        # rect.left, self.right - lewy i prawy kraniec obiektu na ekranie

    def aktualizuj(self):
        self.porusza_sie = 0