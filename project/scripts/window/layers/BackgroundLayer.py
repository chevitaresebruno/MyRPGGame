from .__init__ import *


from pygame import Surface


class BackgroundLayer:
    def __init__(self, color: Color = Color(20, 20, 20)):
        self.__color: Color = color
    
    def draw(self, surface: Surface) -> None:
        surface.fill(self.__color)
        
