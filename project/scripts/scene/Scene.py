from .__init__ import *

from .IGameObject import IGameObject
from scripts.window.layers.Layer import Layer
from scripts.window.layers.BackgroundLayer import BackgroundLayer


class Scene:
    def __init__(self):
        self.__backgroundLayer: BackgroundLayer = None
        self.__layers: list[Layer] = list()
        self.__gameObjects: list[IGameObject] = list()
            
    def addLayer(self, layer: Layer) -> None:
        self.__layers.append(layer)
    
    def getLayers(self) -> list[Layer]:
        return self.__layers
    
    def setBackgroundLayer(self, backgroundLayer: BackgroundLayer) -> None:
        self.__backgroundLayer = backgroundLayer

    def getBackgroundLayer(self) -> BackgroundLayer:
        return self.__backgroundLayer
        
    def mechanics(self) -> InteractiveMechanic:
        mechanics = list()
        for gameObject in self.__gameObjects:
            mechanics.append(*gameObject.mechanics())

        return mechanics

    def addGameObject(self, gameObject: IGameObject) -> None:
        self.__gameObjects.append(gameObject)

