from __init__ import *

from scripts.test.Block import Block
from scripts.test.BlockStates import BlockStates


def main() -> int:
    pg.init()
    
    window = pg.display.set_mode((200, 200))
    fps = 60
    clock = pg.time.Clock()
    
    block = Block(BlockStates.RGB)
    
    spriteGroup = pg.sprite.Group()
    spriteGroup.add(block)
    
    while True:
        clock.tick(fps)
        
        for e in pg.event.get():
            if (e.type == pg.QUIT):
                pg.quit()
                quit()
            
            elif(e.type == pg.KEYDOWN):
                match(e.key):
                    case pg.K_r:
                        block.swapState(BlockStates.RGB)
                    case pg.K_c:
                        block.swapState(BlockStates.CMYK)
                
        window.fill((20, 20, 20))

        spriteGroup.update()
        spriteGroup.draw(window)
        
        pg.display.flip()
                

if __name__ == "__main__":
    main()
    
    