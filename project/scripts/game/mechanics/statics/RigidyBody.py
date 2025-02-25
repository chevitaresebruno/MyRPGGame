from pygame import Rect
from pygame.math import Vector2


from scripts.shared.RectObject import RectObject


class RigidyBody(RectObject):
    def __init__(self):
        RectObject.__init__(self)

    def move(self, vector: Vector2) -> None:
        self.rect.move(vector.x, vector.y)

