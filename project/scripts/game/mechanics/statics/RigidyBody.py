from pygame import Rect
from pygame.math import Vector2


class RigidyBody:
    def __init__(self, rect: Rect):
        self.rect: Rect = rect

    def move(self, vector: Vector2):
        self.rect.move(vector.x, vector.y)

