import random
from constants import *
import pygame

vec = pygame.math.Vector2

class Kulka(pygame.sprite.Sprite):
    def __init__(self, ):
        super().__init__()
        self.obraz = pygame.image.load(f"{file_path}ball.png")
        self.r = 16
        self.zresetuj_pozycje()
        self.przegrana = False

    def zresetuj_pozycje(self):
        self.wspolrzedne = vec(SZEROKOSC / 2, WYSOKOSC - 140)
        self.rect = self.obraz.get_rect(center = self.wspolrzedne)
        self.wektor = vec(0, -10)
        self.kat_nachylenia = random.randint(-30, 30)
        self.wektor.rotate_ip(self. kat_nachylenia)
        self.przegrana = False
    
    def aktualizuj(self, platforma, klocki):
        self.wspolrzedne += self.wektor
        self.rect.center = self.wspolrzedne
        self.sprawdz_kolizje(platforma, klocki)
        #------------------------------------
    def sprawdz_kolizje(self, platforma, klocki):
        if self.rect.left <= 0:
            self.wektor.x *= -1
        if self.rect.right >= SZEROKOSC:
            self.wektor.x *= -1
        if self.rect.top <= 0:
            self.wektor.y *= -1
        if self.rect.bottom >= WYSOKOSC:
            self.przegrana = True

        if self.rect.colliderect(platforma.rect):
            self.wektor.y *= -1

            self.wektor.x += platforma.porusza_sie * ROTACJA
        
            if self.wektor.x < -10: self.wektor.x = -10
            if self.wektor.x > 10: self.wektor.x = 10

        for klocek in klocki:
            if self.kolizja_z_klockiem(self, klocek):
                klocek.uderzenie()
                break
        
    def kolizja_z_klockiem(self, kulka, klocek):
        dystans_x = abs(kulka.rect.centerx - klocek.rect.centerx) - klocek.rect.w / 2 - kulka.r # Była literówka: conter zamiast center
        dystans_y = abs(kulka.rect.centery - klocek.rect.centery) - klocek.rect.h / 2  - kulka.r # Była literówka: conter zamiast center
        
        if dystans_x <= 0 and dystans_y <= 0:
            if dystans_x < dystans_y:
                self.wektor.y *= -1
            else:
                self.wektor.x *= -1 # W miejscu, gdzie następuje odbicie wektora X zrobiłeś odbicie wektora Y
            return True
        return False