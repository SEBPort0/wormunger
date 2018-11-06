from colors import *
from pygame import sprite, Surface
from random import choice

class Segment(sprite.Sprite):
    def __init__(self, x, y, dimension, color=GREEN):
        super(Segment, self).__init__()
        self.image = Surface((dimension, dimension))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = choice([0, -dimension, dimension])
        self.dy = 0

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

class Worm():
    def __init__(self, x, y, numberOfSegments, color=GREEN):
        self.dimension = 15
        self.segments = []
        segment = Segment(x, y, self.dimension, color)
        self.segments.append(segment)

    def changeDxDy(self, dx, dy):
        for segment in self.segments:
            segment.dx = dx
            segment.dy = dy

    def addSegment(self):
        x = self.segments[0].rect.x + self.segments[0].dx
        y = self.segments[0].rect.y + self.segments[0].dy
        segment = Segment(x, y, self.dimension)
        self.segments.insert(0, segment)
        return segment
