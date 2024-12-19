import pygame

pygame.init() # Inicjacja modułu pygame - początek pracy z tą biblioteką

SZEROKOSC = 800
WYSOKOSC = 600
FPS = 60

screen_surface = pygame.display.set_mode((SZEROKOSC, WYSOKOSC)) # Rozmiary okna

pygame.display.set_caption('Pierwsza gra') # Określenie nazwy okna, które się wyświetli

clock = pygame.time.Clock()

def load_image(img_path, position): # img_path - ścieżka z obrazka
    image = pygame.image.load(img_path)
    surface = image.convert()

    transparent_color = (0, 0, 0)
    surface.set_colorkey((transparent_color)) # Zamienia kolor czarny na przezroczysty

    rect = surface.get_rect(center = position) # Pozycja wyświetlania obiektu

    return [image, surface, rect]

def print_image(img_list):
    image, surface, rect = img_list
    screen_surface.blit(surface, rect)
    return

#################################################################

player_pos = [0, 0]#[SZEROKOSC // 2, WYSOKOSC // 2]

player = load_image("Lekcja12/grafiki/player.png", player_pos)

status_gry = True # Flaga określająca, czy gra jest kontynuowana

while status_gry:

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            status_gry = False

    print_image(player)

    pygame.display.update() # Aktualizuje ekran

    clock.tick(FPS)

pygame.quit() # Kończy wykonywanie modułu pygame
quit() # Kończy wykonywanie skryptu