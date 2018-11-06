from colors import *
from pygame import sprite, Surface

class Fruit(sprite.Sprite):
    def __init__(self, x, y, color=RED):
        super(Fruit, self).__init__()
        self.dimension = 15
        self.image = Surface((self.dimension, self.dimension))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def changePosition(self, x, y):
        self.rect.x = x
        self.rect.y = y
