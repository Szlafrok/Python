file_path = 'Lekcja24/Projekt/images/'

import pygame

SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600

obraz_tla = pygame.image.load(file_path + 'background.png')
obraz_postaci = pygame.image.load(file_path + 'base.png')

pygame.init()

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

gra_dziala = True
while gra_dziala:

    zdarzenia = pygame.event.get()
    for zdarzenie in zdarzenia:
        if zdarzenie.type == pygame.QUIT:
            gra_dziala = False
        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False

    ekran.blit(obraz_tla, (0, 0))
    ekran.blit(obraz_postaci, (270, 130))

    pygame.display.flip()

    zegar.tick(30)


pygame.quit()