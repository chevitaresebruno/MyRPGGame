from abc import ABC, abstractmethod

from pygame import Surface


class IDrawble(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def surface(self) -> Surface:
        pass
    
    @abstractmethod
    def position(self) -> Surface:
        pass
    
    