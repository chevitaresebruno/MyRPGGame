from __init__ import *

from scripts.game.Game import Game
from scripts.test.Block import Block
from scripts.test.BlockStates import BlockStates


def main() -> int:
    Game.init()
    
    game = Game(60, (200, 200))
    
    block = Block(BlockStates.RGB)
    
    spriteGroup = pg.sprite.Group()
    spriteGroup.add(block)
    
    game.mainLoop(block, spriteGroup)

    Game.end()

if __name__ == "__main__":
    main()
    
    