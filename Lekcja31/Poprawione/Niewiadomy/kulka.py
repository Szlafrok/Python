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

    def aktualizuj(self, platforma, klocki):
        self.wspolrzendne += self.wektor
        self.rect.center = self.wspolrzendne
        self.sprawdz_kolizje(platforma, klocki)

    
    def sprawdz_kolizje(self, platforma, klocki):
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

            if self.wektor.x < -10: self.wektor.x = -10
            if self.wektor.x > 10: self.wektor.x = 10

        for klocek in klocki:
            if self.kolizja_z_klockiem(self, klocek): # Była literówka w funkcji
                klocek.uderzenie()
                break
        
    def kolizja_z_klockiem(self, kulka, klocek): # Argumenty były zamienione miejscami, przez co program traktował kulkę jako klocek, a klocek jako kulkę
        dystans_x = abs(kulka.rect.centerx - klocek.rect.centerx) - klocek.rect.w / 2 - kulka.r
        dystans_y = abs(kulka.rect.centery - klocek.rect.centery) - klocek.rect.h / 2 - kulka.r

        if dystans_x <= kulka.r and dystans_y <= 0:
            if dystans_x < dystans_y:
                self.wektor.y *= -1
            else:
                self.wektor.x *= -1
            return True
        return False