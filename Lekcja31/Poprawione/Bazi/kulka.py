import random
from constants import *
import pygame

vec = pygame.math.Vector2

class Kulka(pygame.sprite.Sprite):
    def __init__(self):    
        super().__init__()
        self.obraz = pygame.image.load(f"{file_path}ball.png")
        self.zresetuj_pozycje()
        self.r = 16
        self.przegrana = False
    
    def zresetuj_pozycje(self):
        self.wspolrzedne = vec(SZEROKOSC_EKRANU // 2, WYSOKOSC_EKRANU - 140)
        self.rect = self.obraz.get_rect(center = self.wspolrzedne)
        self.wektor = vec(0, -10)
        self.kat_nachylenia = random.randint(-30, 30)
        self.wektor.rotate_ip(self.kat_nachylenia)
        self.przegrana = False
    
    def aktualizuj(self, platforma, klocki):
        self.wspolrzedne += self.wektor
        self.rect.center = self.wspolrzedne
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

            self.wektor.x += platforma.porusza_sie * ROTACJA

            if self.wektor.x < -10: self.wektor.x = -10
            if self.wektor.x > 10: self.wektor.x = 10
        
        for klocek in klocki:
            if self.kolizja_z_klockiem(self, klocek):
                klocek.uderzenie()
                break
    
    def kolizja_z_klockiem(self,kulka, klocek):
        dystans_x = abs(kulka.rect.centerx - klocek.rect.centerx) - klocek.rect.w / 2 - kulka.r
        dystans_y = abs(kulka.rect.centery - klocek.rect.centery) - klocek.rect.h / 2 - kulka.r

        if dystans_x <= 0 and dystans_y <= 0: # było: dystans_x <= kulka.r
            if dystans_x < dystans_y:
                self.wektor.y *= -1
            else:
                self.wektor.x *= -1
            return True # Tu było wcięcie! Zwracasz True, jeżeli masz kolizję (zewnętrzny IF), nie tylko jeżeli odbijasz się od boku (return było wewnątrz ELSE)
        # Mógłbyś tu zwracać False, ale to kwestia elegancji