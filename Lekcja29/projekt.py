import pygame
from constants import *
from platforma import Platforma

pygame.init()
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

obraz_tla = pygame.image.load(f"{file_path}background.png")

platforma = Platforma() # tworzymy obiekt platformy


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

    ekran.blit(obraz_tla, (0, 0)) # wstawiamy tło...
    ekran.blit(platforma.obraz, platforma.rect) #... i platformę!

    pygame.display.flip()

    zegar.tick(30) # 30 klatek na sekundę

pygame.quit()