from __init__ import *


from scripts.time.Ticker import Ticker
from .window.Window import Window

from scripts.test.BlockStates import BlockStates


class Game:
    def __init__(self, fps: int, windowSize: tuple[int, int]):
        self.__ticker = Ticker(fps)
        self.__window = Window(windowSize)
        
    @staticmethod
    def init() -> None:
        pg.init()
    
    @staticmethod
    def end() -> None:
        pg.quit()        
    
    def mainLoop(self, block, spriteGroup) -> None:
        self.__ticker.update()
        self.__window.load(SCENES_DIR / "test.xml")
        
        while True:
            for e in pg.event.get():
                if (e.type == pg.QUIT):
                    return
                elif(e.type == pg.KEYDOWN):
                    match(e.key):
                        case pg.K_r:
                            block.swapState(BlockStates.RGB)
                        case pg.K_c:
                            block.swapState(BlockStates.CMYK)

            self.__window.draw()
            
            spriteGroup.update()
            spriteGroup.draw(self.__window.surface)
            
            pg.display.flip()