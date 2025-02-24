from .__init__ import *


class BackgroundLayer(IDrawble):
    def __init__(self, color: Color = Color(20, 20, 20)):
        self.__color = color
    
    def draw(self, surface: Surface) -> None:
        surface.fill(self.__color)
        
        