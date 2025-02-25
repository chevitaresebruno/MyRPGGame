from abc import ABC, abstractmethod

from pygame import Surface


class IDrawble(ABC):
    def __init__(self):
        ABC.__init__(self)
    
    @abstractmethod
    def surface(self) -> Surface:
        pass
    
    @abstractmethod
    def position(self) -> Surface:
        pass
    
    