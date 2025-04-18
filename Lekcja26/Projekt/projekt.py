import pygame
import random
from Jablko import Jablko
from file_path import file_path

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

    ekran.blit(tlo, (0, 0))

    for jablko in jablka:
        ekran.blit(jablko.obraz, jablko.rect)

    pygame.display.flip()

    zegar.tick(30)


pygame.quit()