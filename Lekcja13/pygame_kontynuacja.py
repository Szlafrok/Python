import pygame

pygame.init() # Inicjacja modułu pygame - początek pracy z tą biblioteką

SZEROKOSC = 800
WYSOKOSC = 600
FPS = 60

screen_surface = pygame.display.set_mode((SZEROKOSC, WYSOKOSC)) # Rozmiary okna

pygame.display.set_caption('Pierwsza gra') # Określenie nazwy okna, które się wyświetli

clock = pygame.time.Clock()

def load_image(img_path, position): # img_path - ścieżka z obrazka
    pass

def print_image():
    pass

#################################################################

load_image("Lekcja12/grafiki/player.png", None)

status_gry = True # Flaga określająca, czy gra jest kontynuowana

while status_gry:

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            status_gry = False

    pygame.display.update() # Aktualizuje ekran

    clock.tick(FPS)

pygame.quit() # Kończy wykonywanie modułu pygame
quit() # Kończy wykonywanie skryptu