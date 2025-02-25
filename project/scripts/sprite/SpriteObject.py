from .__init__ import *

from pygame.sprite import Sprite

from scripts.time.Timer import Timer
from scripts.shared.RectObject import RectObject
from scripts.window.interface.IDrawble import IDrawble

from .Repository import Repository


class SpriteObject(Sprite, RectObject, IDrawble):
    def __init__(self, repository: Repository, state: Enum):
        Sprite.__init__(self)
        RectObject.__init__(self)
        
        self.__repository: Repository = repository
        self.__state: Enum = state

        self.image: Surface = self.__repository.getFirst()
        self.rect = self.image.get_rect()  # Come from Rect Object

        self.__current: int = 0
        self.__timer = Timer(self.__repository.timeUpdate(self.__state))
    
    def update(self) -> None:
        if(self.__timer.canUpdate()):
            self.__current = (self.__current+1) % self.__repositorySize()
            self.__getActual()
    
    def __getActual(self) -> None:
        self.image = self.__repository.getByState(self.__state)[self.__current]
    
    def __repositorySize(self) -> int:
        return len(self.__repository.getByState(self.__state))
    
    def swapState(self, new: Enum):
        self.__state = new
        self.__timer.__increment = self.__repository.timeUpdate(self.__state)
        self.__current = 0
        self.__getActual()
        self.__timer.reset()
            
    def surface(self) -> Surface:
        return self.image
    
    def position(self) -> Rect:
        return self.rect

