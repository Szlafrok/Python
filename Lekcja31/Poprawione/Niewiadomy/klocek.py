import pygame
from constants import *
import copy

class Klocek(pygame.sprite.Sprite):
    def __init__(self, x, y, zdrowie):
        super().__init__()
        self.obraz_orginalny = pygame.image.load(f"{file_path}brick.png")
        self.rect = pygame.Rect(x, y, 96, 48)
        self.zdrowie = zdrowie

    def aktualizuj(self):
        maska_koloru = 0
        if self.zdrowie == 3:
            maska_koloru = (128, 0, 0)
        if self.zdrowie == 2:
            maska_koloru = (0, 0, 128)
        if self.zdrowie == 1:
            maska_koloru = (0, 128, 128)
        self.obraz = copy.copy(self.obraz_orginalny)
        self.obraz.fill(maska_koloru, special_flags=pygame.BLEND_ADD)

    def update(self):
        self.aktualizuj()

    def uderzenie(self):
        self.zdrowie -= 1
        if self.zdrowie <= 0:
            self.kill()