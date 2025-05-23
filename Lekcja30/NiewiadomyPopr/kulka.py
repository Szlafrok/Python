import random
import pygame
from constants import *

vec = pygame.math.Vector2

class Kulka(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.obraz = pygame.image.load(f"{file_path}ball.png")
        self.zresetuj_pozycje()
        self.r = 16
        self.przegrana = False

    def zresetuj_pozycje(self):
        self.wspolrzendne = vec(SZEROKOSC_EKRANU / 2, WYSOKOSC_EKRANU - 140)
        self.rect = self.obraz.get_rect(center = self.wspolrzendne)
        self.wektor = vec(0, -10)
        self.kat_nachylenia = random.randint(-30, 30)
        self.wektor.rotate_ip(self.kat_nachylenia)
        self.przegrana = False

    def aktualizuj(self, platforma):
        self.wspolrzendne += self.wektor
        self.rect.center = self.wspolrzendne
        self.sprawdz_kolizje(platforma)
    
    def sprawdz_kolizje(self, platforma):
        if self.rect.x <= 0:
            self.wektor.x *= -1
        if self.rect.right >= SZEROKOSC_EKRANU:
            self.wektor.x *= -1
        if self.rect.y <= 0:
            self.wektor.y *= -1
        if self.rect.bottom >= WYSOKOSC_EKRANU:
            self.przegrana = True

        if self.rect.colliderect(platforma.rect):
            self.wektor.y *= -1
            
            self.wektor.x += platforma.poruszaj_sie * ROTACJA

            if self.wektor.x < -10: self.wektor.x = -10 # Tu brakowało minusa w warunku!
            if self.wektor.x > 10: self.wektor.x = 10