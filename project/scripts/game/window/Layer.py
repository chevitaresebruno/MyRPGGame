from .__init__ import *


class Layer(IDrawble):
    def __init__(self):
        self.__objects: list[Surface] = list()
    
    def draw(self, surface: Surface) -> None:
        for obj in self.__objects:
            surface.blit(obj)
            
    def add(self, obj: Surface):
        self.__objects.append(obj)
        
        