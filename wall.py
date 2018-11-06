from pygame import sprite, Surface
from pygame.locals import *
from colors import *

class Wall(sprite.Sprite):
    def __init__(self, x, y, width, height, color=WHITE):
        super(Wall, self).__init__()
        self.image = Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
