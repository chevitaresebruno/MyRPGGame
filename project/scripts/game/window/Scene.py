from .__init__ import *


class Scene(IDrawble):
    def __init__(self):
        self.__layers: list[IDrawble] = list()
        
    def draw(self, surface: Surface) -> None:
        for layer in self.__layers:
            layer.draw(surface)
            
    def add(self, layer: IDrawble) -> None:
        self.__layers.append(layer)
        
        