import random
import pygame

from constants_s import *

class Jablko(pygame.sprite.Sprite):
    def __init__(self):
        super(Jablko, self).__init__()
        self.obraz = pygame.image.load(f"{file_path}apple.png")
        self.rect = pygame.Rect((32 * random.randint(0, 24), 32 * random.randint(0, 18), 32, 32))