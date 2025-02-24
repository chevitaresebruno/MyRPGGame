from .__init__ import *

from pathlib import Path
import xml.etree.ElementTree as ET

from .Layer import Layer
from .Scene import Scene
from .ScenesTags import ScenesTags
from .BackgroundLayer import BackgroundLayer


class Window:
    def __init__(self, size: tuple[int]):
        self.__window: Scene = set_mode(size)
        self.__scene: Scene = None
        
    def update(self) -> None:
        self.__window.fill()
        
    def load(self, scene: Path) -> None:
        tree = ET.parse(scene)
        main = tree.getroot()
        
        self.__scene = Scene()
        
        for element in main:
            match element.tag:
                case ScenesTags.BACKGROUND.value:
                    self.__scene.add(BackgroundLayer([int(x) for x in element.text.split()]))
                case ScenesTags.LAYER.value:
                    pass
    
    def draw(self):
        self.__scene.draw(self.__window)
        
    @property
    def surface(self) -> Surface:
        return self.__window
    
    