import pygame
import random
from constants_s import *
from Jablko import Jablko
from Jajo import Jajo
from Waz import Waz
from Kierunek import Kierunek

tlo = pygame.Surface([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])

for i in range(25):
    for j in range(19):
        obraz = pygame.image.load(f"{file_path}background.png")
        maska = (random.randint(0, 20), random.randint(0, 20), random.randint(0, 20))

        obraz.fill(maska, special_flags = pygame.BLEND_ADD)
        tlo.blit(obraz, (i * 32, j * 32))

pygame.init()
pygame.font.init()

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

moja_czcionka = pygame.font.SysFont("Consolas", 24) # cokolwiek tylko nie Comic Sans

pygame.display.set_caption("Snake Python")

waz = Waz()
PORUSZ_WEZEM = pygame.USEREVENT + 1
pygame.time.set_timer(PORUSZ_WEZEM, 200)

jablko = Jablko()
jablka = pygame.sprite.Group()
jablka.add(jablko)

jaja = pygame.sprite.Group()

jajo_stworzone = False

gra_dziala = True
while gra_dziala:
    zdarzenia = pygame.event.get()
    for zdarzenie in zdarzenia:
        if zdarzenie.type == pygame.QUIT:
            gra_dziala = False
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
            if zdarzenie.key == pygame.K_w or zdarzenie.key == pygame.K_UP:
                waz.zmien_kierunek(Kierunek.GORA)
            if zdarzenie.key == pygame.K_d or zdarzenie.key == pygame.K_RIGHT:
                waz.zmien_kierunek(Kierunek.PRAWO)
            if zdarzenie.key == pygame.K_s or zdarzenie.key == pygame.K_DOWN:
                waz.zmien_kierunek(Kierunek.DOL)
            if zdarzenie.key == pygame.K_a or zdarzenie.key == pygame.K_LEFT:
                waz.zmien_kierunek(Kierunek.LEWO)
        if zdarzenie.type == PORUSZ_WEZEM:
            waz.aktualizuj()

    kolizja_z_jablkiem = pygame.sprite.spritecollideany(waz, jablka)
    if kolizja_z_jablkiem != None:
        kolizja_z_jablkiem.kill()
        waz.mniam()
        jablko = Jablko()
        jablka.add(jablko)

    kolizja_z_jajkiem = pygame.sprite.spritecollideany(waz, jaja)
    if kolizja_z_jajkiem != None:
        gra_dziala = False

    ekran.blit(tlo, (0, 0))

    for jablko in jablka:
        ekran.blit(jablko.obraz, jablko.rect)
    
    for jajo in jaja:
        ekran.blit(jajo.obraz, jajo.rect)

    if waz.liczba_zjedzonych_jablek % 10 == 0 and waz.liczba_zjedzonych_jablek != 0 and not jajo_stworzone:
        if waz.segmenty and waz.segmenty[-1].ostatnia_pozycja is not None:
            jajo = Jajo(waz.segmenty[-1].ostatnia_pozycja)
            jaja.add(jajo)
            jajo_stworzone = True
    
    if waz.liczba_zjedzonych_jablek % 10 != 0:
        jajo_stworzone = False

    ekran.blit(waz.obraz, waz.rect)
    waz.rysuj_segmenty(ekran)

    if waz.sprawdz_kolizje():
        gra_dziala = False

    pygame.display.flip()

    zegar.tick(30)
    
czas_gry = pygame.time.get_ticks()
print(f"Czas gry: {czas_gry / 1000:.1f} s")
print(f"Liczba zjedzonych jabłek: {waz.liczba_zjedzonych_jablek}") # dodałem to ponieważ przy np. 30 segmentach niezdąży się ich policzyć bo się w ściane wejdzie
pygame.quit()