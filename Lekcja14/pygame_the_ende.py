# Import modulu pygame, dzieki ktoremu tworzymy aplikacje okienkowa
import pygame
 
# Inicjalizacja modułu
pygame.init()
# Utworzenie okna o określonych wymiarach
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Pierwsza Gra') # Nadanie nazwy oknu
 
clock = pygame.time.Clock() # Utworzenie zegara, który nadzoruje stałe wartości fps
 
def load_image(img_path: str, position):
    image = pygame.image.load(img_path)
    surface = image.convert()
 
    transparent_color = (0, 0, 0)
    surface.set_colorkey(transparent_color)

    rect = surface.get_rect(center=position) # Pozycja wyświetlania obiektu zapisana jest w rect
 
    return [image, surface, rect]
 
 
def print_image(img_list) -> None:
    #img_list: [image, surface, rect]
    image, surface, rect = img_list
    screen_surface.blit(surface, rect)
    return

def set_position_image(img_list, position): # img_list = [image, surface, rect]
    image, surface, rect = img_list
    rect = surface.get_rect(center=position)
    return [image, surface, rect]

def calculate_player_movement(keys): # Poruszanie postacią
    speed = 10
    delta_x = 0
    delta_y = 0
    if keys[pygame.K_w]: # dla WASD: [True, False, False, False] ##### pygame.K_w == 0
        delta_y -= speed
    if keys[pygame.K_s]:
        delta_y += speed
    if keys[pygame.K_d]:
        delta_x += speed
    if keys[pygame.K_a]:
        delta_x -= speed
    return [delta_x, delta_y]

def limit_position(position: list) -> list:
    x, y = position
    x = min(SCREEN_WIDTH, x) # Ograniczenie z prawej
    x = max(0, x) # Ograniczenie z lewej
    y = min(SCREEN_HEIGHT, y)
    y = max(y, 0)
    return [x, y]


################################################

player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image('Lekcja12/grafiki/player.png', player_pos)
 
background_color = [0, 0, 20]

game_status = True # Flag określająca, czy należy zamknąć okno

while game_status: # Kod wykonywany póki aplikacja jest uruchomiona

    events = pygame.event.get() # Odczytanie zdarzeń zarejestrowanych przez komputer
    for event in events:
        if event.type == pygame.QUIT: # Naciśnięto X - zamykanie aplikacji
            game_status = False
 
    pressed_keys = pygame.key.get_pressed()
    delta_x, delta_y = calculate_player_movement(pressed_keys)
    
    player_pos[0] += delta_x
    player_pos[1] += delta_y

    player_pos = limit_position(player_pos)
    player = set_position_image(player, player_pos)

    screen_surface.fill(background_color)
    print_image(player) # Wyświetl gracza

    pygame.display.update() # Odświeżenie wyświetlanego okna
 
    clock.tick(60)
 
print("Zamykanie aplikacji")

pygame.quit() # Zamknięcie aplikacji
quit() # Zamknięcie skryptu


