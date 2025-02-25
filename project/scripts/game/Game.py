from __init__ import *


from scripts.time.Ticker import Ticker
from .window.Window import Window
from .window.Scene import Scene

from .events.EventController import EventController
from .events.ExitAction import ExitAction

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

    def load(self, scene: Scene) -> None:
        self.__window.load(scene)
        self.__eventController.clear()
        self.__eventController.loadMechanics(scene.mechanics())
        self.__eventController.loadEvent(self.__looper.toLoad())

    def mainLoop(self) -> None:
        self.__ticker.update()
        
        while self.__looper.infinityLoop:
            self.__eventController.loop()

            self.__window.draw()
            
            pg.display.flip()

