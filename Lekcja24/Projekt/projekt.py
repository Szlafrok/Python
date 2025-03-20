file_path = 'Lekcja24/Projekt/images/'

import pygame # Wczytanie modułu Pygame

SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600

obraz_tla = pygame.image.load(file_path + 'background.png') # Tworzymy obiekt, którzy przechowuje obraz
obraz_postaci = pygame.image.load(file_path + 'base.png')

pygame.init() # Inicjujemy moduł

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU]) # Tworzymy obiekt ekranu ORAZ OKNO
zegar = pygame.time.Clock() # Tworzymy obiekt zegara

gra_dziala = True
while gra_dziala:

    zdarzenia = pygame.event.get() # Lista zdarzeń w Pygame
    for zdarzenie in zdarzenia:
        if zdarzenie.type == pygame.QUIT: # typ zdarzenia - zamknięcie okna znakiem X
            gra_dziala = False
        elif zdarzenie.type == pygame.KEYDOWN: # typ zdarzenia - wciśnięty klawisz
            if zdarzenie.key == pygame.K_ESCAPE: # okreslenie wciśniętego klawisza jako ESCAPE
                gra_dziala = False

    ekran.blit(obraz_tla, (0, 0)) # dodanie do generowanego ekranu obrazu tła
    ekran.blit(obraz_postaci, (270, 130)) # dodanie do generowanego ekranu obrazu postaci

    pygame.display.flip() # aktualizacja ekranu

    zegar.tick(30) # ograniczenie klatek na sekundę do 30


pygame.quit() # zakończenie używania pygame