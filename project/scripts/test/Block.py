from scripts.sprite.SpriteObject import SpriteObject
from .BlockRepository import BlockRepository
from .BlockStates import BlockStates


class Block(SpriteObject):
    def __init__(self, initialState: BlockStates):
        SpriteObject.__init__(self, BlockRepository(), initialState)
        
        