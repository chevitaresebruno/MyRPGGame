from scripts.game.mechanics.interactives.movement.TopDownMovement import TopDownMovement
from scripts.sprite.SpriteObject import SpriteObject
from scripts.game.window.IGameObject import IGameObject

from scripts.test.BlockStates import BlockStates
from scripts.test.BlockRepository import BlockRepository

from pygame.math import Vector2


class Player(TopDownMovement, SpriteObject, IGameObject):
    def __init__(self, startPos: list[int]):
        TopDownMovement.__init__(self)
        SpriteObject.__init__(self, BlockRepository(), BlockStates.RGB)
        
        self.move(Vector2(startPos))

    def mechanics(self):
        return [self,]
        
        