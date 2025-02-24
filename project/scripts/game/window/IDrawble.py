from abc import ABC, abstractmethod


class IDrawble(ABC):
    def __init__(self):
        super().__init__()
        
    @abstractmethod
    def draw(self) -> None:
        pass
    
    