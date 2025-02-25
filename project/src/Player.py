from pygame.math import Vector2


from scripts.test.BlockStates import BlockStates
from scripts.scene.IGameObject import IGameObject
from scripts.sprite.SpriteObject import SpriteObject
from scripts.test.BlockRepository import BlockRepository
from scripts.mechanics.interactives.movement.TopDownMovement import TopDownMovement


class Player(TopDownMovement, SpriteObject, IGameObject):
    def __init__(self, startPos: list[int]):
        TopDownMovement.__init__(self)
        SpriteObject.__init__(self, BlockRepository(), BlockStates.RGB)
        
        self.move(Vector2(startPos))

    def mechanics(self):
        return [self,]
        
        