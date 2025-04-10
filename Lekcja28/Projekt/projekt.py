import pygame
import random
from Jablko import Jablko
from file_path import file_path
from Waz import Waz
from Kierunek import Kierunek

SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 608
tlo = pygame.Surface([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])

for i in range(25):
    for j in range(19):
        obraz = pygame.image.load(f"{file_path}background.png")
        maska = (random.randint(0, 20), random.randint(0, 20), random.randint(0, 20))

        obraz.fill(maska, special_flags = pygame.BLEND_ADD)
        tlo.blit(obraz, (i * 32, j * 32))

pygame.init()
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

pygame.display.set_caption("Snake Python")


waz = Waz()
PORUSZ_WEZEM = pygame.USEREVENT + 1
pygame.time.set_timer(PORUSZ_WEZEM, 200)


jablko = Jablko()
jablka = pygame.sprite.Group()
jablka.add(jablko)


gra_dziala = True
while gra_dziala:
    zdarzenia = pygame.event.get()
    for zdarzenie in zdarzenia:
        if zdarzenie.type == pygame.QUIT:
            gra_dziala = False
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
            if zdarzenie.key == pygame.K_w:
                waz.zmien_kierunek(Kierunek.GORA)
            if zdarzenie.key == pygame.K_d:
                waz.zmien_kierunek(Kierunek.PRAWO)
            if zdarzenie.key == pygame.K_s:
                waz.zmien_kierunek(Kierunek.DOL)
            if zdarzenie.key == pygame.K_a:
                waz.zmien_kierunek(Kierunek.LEWO)
        if zdarzenie.type == PORUSZ_WEZEM:
            waz.aktualizuj()

    kolizja_z_jablkiem = pygame.sprite.spritecollideany(waz, jablka)
    if kolizja_z_jablkiem != None:
        kolizja_z_jablkiem.kill()
        waz.mniam()
        jablko = Jablko()
        jablka.add(jablko)

    ekran.blit(tlo, (0, 0))

    for jablko in jablka:
        ekran.blit(jablko.obraz, jablko.rect)

    ekran.blit(waz.obraz, waz.rect)
    waz.rysuj_segmenty(ekran)

    if waz.sprawdz_kolizje():
        gra_dziala = False

    pygame.display.flip()

    zegar.tick(30)

pygame.quit()