import pygame
from constants import *
from patforma import Platforma
from kulka import Kulka
from klocek import Klocek

pygame.init()
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("Arcanoid")
zegar = pygame.time.Clock()

tlo_obraz = pygame.image.load(f"{file_path}background.png")

czcionka = pygame.font.SysFont("Arial", 24)
    
start_time = pygame.time.get_ticks()
platforma = Platforma()
kulka = Kulka()

zycie = ZYCIA
poziom = 0

# poziomy gry
poziom1 = [
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
poziom2 = [
    [0, 0, 1, 2, 3, 3, 2, 1, 0, 0],
    [0, 1, 1, 1, 2, 2, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 2, 0, 0, 2, 0, 2, 0]
]
poziom3 = [
    [2, 3, 2, 2, 2, 2, 2, 2, 3, 2],
    [2, 1, 3, 1, 1, 1, 1, 3, 1, 2],
    [2, 3, 1, 3, 1, 1, 3, 1, 3, 2],
    [3, 2, 2, 2, 3, 3, 2, 2, 2, 3],
    [0, 0, 2, 2, 3, 3, 2, 2, 0, 0],
    [0, 0, 2, 0, 3, 3, 0, 2, 0, 0],
    [0, 0, 3, 0, 3, 3, 0, 3, 0, 0]
]

klocki = pygame.sprite.Group()
def dodaj_klocki():
    wczytany_poziom = None
    if poziom == 0:
        wczytany_poziom = poziom1
    elif poziom == 1:
        wczytany_poziom = poziom2
    else:
        wczytany_poziom = poziom3
    
    for i in range(10):
        for j in range(7):
            if wczytany_poziom[j][i] != 0:
                klocek = Klocek(32 + i*96, 32 + j*48, wczytany_poziom[j][i])
                klocki.add(klocek)
dodaj_klocki()

gra_dziala = True
while gra_dziala:
    zdarzenia = pygame.event.get()
    for zdarzenie in zdarzenia:
        if zdarzenie.type == pygame.QUIT:
            gra_dziala = False
        elif zdarzenie.type == pygame.KEYDOWN:
            #gra_dziala = False
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        platforma.ruszaj_platforma(-1)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        platforma.ruszaj_platforma(1)

    if len(klocki.sprites()) == 0:
        poziom += 1
        if poziom >= 3 :
            break
        kulka.zresetuj_pozycje()
        platforma.resetuj_pozycje()
        dodaj_klocki()
    
    kulka.aktualizuj(platforma, klocki)
    klocki.update()
    platforma.aktualizuj()

    if kulka.przegrana:
        zycie -= 1
        if zycie <= 0:
            gra_dziala = False
        else:    
            kulka.zresetuj_pozycje()
            platforma.resetuj_pozycje()

    ekran.blit(tlo_obraz, (0, 0))
    ekran.blit(platforma.obraz, platforma.rect)
    ekran.blit(kulka.obraz, kulka.rect)
    for klocek in klocki:
        ekran.blit(klocek.obraz, klocek.rect)
    
    tekst = czcionka.render(f"Życia: {zycie}", False,(255, 255, 255))
    ekran.blit(tekst,(16,0))
    
    pygame.display.flip()

    zegar.tick(30)

pygame.quit()