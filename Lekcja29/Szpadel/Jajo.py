import random
import pygame

from constants_s import *

class Jajo(pygame.sprite.Sprite):
    def __init__(self, pozycja):
        super(Jajo, self).__init__()
        self.obraz = pygame.image.load(f"{file_path}egg.png")
        self.rect = pygame.Rect((pozycja.x, pozycja.y, 32, 32))