from pygame import Surface
from pygame.display import set_mode

from scripts.scene.Scene import Scene


class Window:
    def __init__(self, size: tuple[int]):
        self.__window: Surface = set_mode(size)
        self.__scene: Scene = None
        
    def update(self) -> None:
        self.__window.fill()
        
    def load(self, scene: Scene) -> None:
        self.__scene = scene
    
    def draw(self):
        self.__scene.getBackgroundLayer().draw(self.__window)
        for layer in self.__scene.getLayers():
            for obj in layer:
                self.__window.blit(obj.surface(), obj.position())
        
    @property
    def surface(self) -> Surface:
        return self.__window
    
    