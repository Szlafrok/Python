import pygame
from Kierunek import Kierunek
from file_path import file_path

class Waz(pygame.sprite.Sprite):
    def __init__(self):
        self.oryginalny_obraz = pygame.image.load(f"{file_path}head.png")
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, 0)
        self.rect = self.obraz.get_rect(center = (12*32+16, 9*32+16))