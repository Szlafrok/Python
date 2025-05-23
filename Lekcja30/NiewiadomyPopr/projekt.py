import pygame
from constants import *
from platforma import Platforma
from kulka import Kulka

pygame.init()
pygame.font.init()

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

czcionka = pygame.font.SysFont("Arial", 24)

zycia = ZYCIA

obraz_tla = pygame.image.load(f"{file_path}background.png")

platforma = Platforma() # tworzymy obiekt platformy
kulka = Kulka()

gra_dziala = True
while gra_dziala:
    zdarzenia = pygame.event.get() # zaciągamy listę zdarzeń
    for zdarzenie in zdarzenia:
        if zdarzenie.type == pygame.QUIT:
            gra_dziala = False
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False

    keys = pygame.key.get_pressed() # zaciągamy listę wciśniętych klawiszy
    if keys[pygame.K_a]:
        platforma.ruszaj_platforma(-1)
    if keys[pygame.K_d]:
        platforma.ruszaj_platforma(1)

    kulka.aktualizuj(platforma)
    platforma.aktualizuj()

    if kulka.przegrana:
        zycia -= 1
        if zycia <= 0:
            pygame.quit()
        kulka.zresetuj_pozycje()
        platforma.resetuj_pozycje()

    ekran.blit(obraz_tla, (0, 0)) # wstawiamy tło...
    ekran.blit(platforma.obraz, platforma.rect) #... i platformę!
    ekran.blit(kulka.obraz, kulka.rect)

    tekst = czcionka.render(f"Życia: {zycia}", False, (255, 255, 255))
    ekran.blit(tekst, (16, 0))

    pygame.display.flip()

    zegar.tick(30) # 30 klatek na sekundę

pygame.quit()