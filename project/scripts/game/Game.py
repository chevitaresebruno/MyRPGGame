from __init__ import *


from scripts.time.Ticker import Ticker
from .window.Window import Window
from .events.EventController import EventController
from .events.ExitAction import ExitAction

from .mechanics.interactives.movement.TopDownMovement import TopDownMovement

from scripts.test.BlockStates import BlockStates

# TESTS
from scripts.test.BlockImage import BlockImage
from scripts.tools.Colors import RED

class Game:
    def __init__(self, fps: int, windowSize: tuple[int, int]):
        self.__ticker = Ticker(fps)
        self.__window = Window(windowSize)
        self.__eventController = EventController()
        self.__looper = ExitAction()

        self.__eventController.loadEvent(self.__looper.toLoad())
        
    @staticmethod
    def init() -> None:
        pg.init()
    
    @staticmethod
    def end() -> None:
        pg.quit()        
    
    def mainLoop(self, block, spriteGroup) -> None:
        self.__ticker.update()
        self.__window.load(SCENES_DIR / "test.xml")

        mov = TopDownMovement((0, 0))
        _block = BlockImage.build(RED, (20, 20))
        mov._TopDownMovement__rigidyBody.rect = _block.get_rect()

        self.__eventController.loadMechanic(mov)
        
        while self.__looper.infinityLoop:
            self.__eventController.loop()

            """
            for e in pg.event.get():
                if (e.type == pg.QUIT):
                    return
                elif(e.type == pg.KEYDOWN):
                    match(e.key):
                        case pg.K_r:
                            block.swapState(BlockStates.RGB)
                        case pg.K_c:
                            block.swapState(BlockStates.CMYK)
            """

            self.__window.draw()
            self.__window.surface.blit(_block, mov._TopDownMovement__rigidyBody.rect)
            
            """
            spriteGroup.update()
            spriteGroup.draw(self.__window.surface)
            """

            pg.display.flip()