import pygame

# Inicjalizacja modułu
pygame.init() 

#Utworzenie okna o wymiarach 400x300
surface = pygame.display.set_mode((400, 300))

# Nadanie nazwy oknu
pygame.display.set_caption('Gigantowa Aplikacja')

# Odczytanie zdarzeń zarejestrowanych przez komputer
events = pygame.event.get()

# Odświeżenie wyświetlanego okna
pygame.display.update()

# Zamknięcie aplikacji
pygame.quit()

# Zamknięcie skryptu
quit()

# Iterowanie po otrzymanych wydarzeniach zarejestrowanych przez komputer pozwala na
# wykrywanie konkretnych zdarzeń. Najczęściej używane:
# - QUIT
# - KEYDOWN
# - KEYUP
# - MOUSEMOTION
# - MOUSEBUTTONUP
# - MOUSEBUTTONDOWN
# - text